# SPDX-FileCopyrightText: 2020 The Magma Authors.
# SPDX-FileCopyrightText: 2022 Open Networking Foundation <support@opennetworking.org>
#
# SPDX-License-Identifier: BSD-3-Clause

# pylint: disable=broad-except

import asyncio
import logging
from enum import Enum

import grpc
from google.protobuf import message as proto_message
from google.protobuf.json_format import MessageToJson
from common.service_registry import ServiceRegistry
from orc8r.protos import common_pb2


class RetryableGrpcErrorDetails(Enum):
    """
    Enum for gRPC retryable error detail messages
    """
    SOCKET_CLOSED = "Socket closed"
    CONNECT_FAILED = "Connect Failed"


def return_void(func):
    """
    Reusable decorator for returning common_pb2.Void() message.
    """

    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return common_pb2.Void()

    return wrapper


def grpc_wrapper(func):
    """
    Wraps a function with a gRPC wrapper which creates a RPC client to
    the service and handles any RPC Exceptions.

    Usage:
    @grpc_wrapper
    def func(client, args):
        pass
    func(args, ProtoStubClass, 'service')
    """

    def wrapper(*alist):
        args = alist[0]
        stub_cls = alist[1]
        service = alist[2]
        chan = ServiceRegistry.get_rpc_channel(service, ServiceRegistry.LOCAL)
        client = stub_cls(chan)
        try:
            func(client, args)
        except grpc.RpcError as err:
            print("Error! [%s] %s" % (err.code(), err.details()))
            exit(1)

    return wrapper


def cloud_grpc_wrapper(func):
    """
    Wraps a function with a gRPC wrapper which creates a RPC client to
    the service and handles any RPC Exceptions.

    Usage:
    @cloud_grpc_wrapper
    def func(client, args):
        pass
    func(args, ProtoStubClass, 'service')
    """

    def wrapper(*alist):
        args = alist[0]
        stub_cls = alist[1]
        service = alist[2]
        chan = ServiceRegistry.get_rpc_channel(service, ServiceRegistry.CLOUD)
        client = stub_cls(chan)
        try:
            func(client, args)
        except grpc.RpcError as err:
            print("Error! [%s] %s" % (err.code(), err.details()))
            exit(1)

    return wrapper


def set_grpc_err(
    context: grpc.ServicerContext,
    code: grpc.StatusCode,
    details: str,
):
    """
    Sets status code and details for a gRPC context. Removes commas from
    the details message (see https://github.com/grpc/grpc-node/issues/769)
    """
    context.set_code(code)
    context.set_details(details.replace(',', ''))


def _grpc_async_wrapper(f, gf):
    try:
        f.set_result(gf.result())
    except Exception as e:
        f.set_exception(e)


def grpc_async_wrapper(gf, loop=None):
    """
    Wraps a GRPC result in a future that can be yielded by asyncio

    Usage:

    async def my_fn(param):
        result =
            await grpc_async_wrapper(stub.function_name.future(param, timeout))

    Code taken and modified from:
        https://github.com/grpc/grpc/wiki/Integration-with-tornado-(python)
    """
    f = asyncio.Future()
    if loop is None:
        loop = asyncio.get_event_loop()
    gf.add_done_callback(
        lambda _: loop.call_soon_threadsafe(_grpc_async_wrapper, f, gf),
    )
    return f


def is_grpc_error_retryable(error: grpc.RpcError) -> bool:
    status_code = error.code()
    error_details = error.details()
    if status_code == grpc.StatusCode.UNAVAILABLE and \
            any(
                err_msg.value in error_details for err_msg in
                RetryableGrpcErrorDetails
            ):
        # server end closed connection.
        return True
    return False


def print_grpc(
    message: proto_message.Message, print_grpc_payload: bool,
    message_header: str = "",
):
    """
    Prints content of grpc message

    Args:
        message: grpc message to print
        print_grpc_payload: flag to enable/disable printing of the message
        message_header: header to print before printing grpc content
    """

    if print_grpc_payload:
        log_msg = "{} {}".format(
            message.DESCRIPTOR.full_name,
            MessageToJson(message),
        )
        # add indentation
        padding = 2 * ' '
        log_msg = ''.join(
            "{}{}".format(padding, line)
            for line in log_msg.splitlines(True)
        )
        log_msg = "GRPC message:\n{}".format(log_msg)

        if message_header:
            logging.info(message_header)
        logging.info(log_msg)

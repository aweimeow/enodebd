# SPDX-FileCopyrightText: 2020 The Magma Authors.
# SPDX-FileCopyrightText: 2022 Open Networking Foundation <support@opennetworking.org>
#
# SPDX-License-Identifier: BSD-3-Clause

import logging

import grpc
from google.protobuf.json_format import MessageToDict
from common.service_registry import ServiceRegistry
from orc8r.protos.eventd_pb2 import Event
from orc8r.protos.eventd_pb2_grpc import EventServiceStub

EVENTD_SERVICE_NAME = "eventd"
DEFAULT_GRPC_TIMEOUT = 10


def log_event(event: Event) -> None:
    """
    Make RPC call to 'LogEvent' method of local eventD service
    """
    try:
        chan = ServiceRegistry.get_rpc_channel(
            EVENTD_SERVICE_NAME, ServiceRegistry.LOCAL,
        )
    except ValueError:
        logging.error("Cant get RPC channel to %s", EVENTD_SERVICE_NAME)
        return
    client = EventServiceStub(chan)
    try:
        # Location will be filled in by directory service
        client.LogEvent(event, DEFAULT_GRPC_TIMEOUT)
    except grpc.RpcError as err:
        if err.code() == grpc.StatusCode.UNAVAILABLE:
            logging.debug(
                "LogEvent will not occur unless eventd configuration "
                "is set up.",
            )
        else:
            logging.error(
                "LogEvent error for event: %s, [%s] %s",
                MessageToDict(event),
                err.code(),
                err.details(),
            )

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from lte.protos import s1ap_service_pb2 as lte_dot_protos_dot_s1ap__service__pb2
from orc8r.protos import common_pb2 as orc8r_dot_protos_dot_common__pb2


class S1apServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetENBState = channel.unary_unary(
                '/magma.lte.S1apService/GetENBState',
                request_serializer=orc8r_dot_protos_dot_common__pb2.Void.SerializeToString,
                response_deserializer=lte_dot_protos_dot_s1ap__service__pb2.EnbStateResult.FromString,
                )


class S1apServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetENBState(self, request, context):
        """Returns state of the S1 connected eNBs
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_S1apServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetENBState': grpc.unary_unary_rpc_method_handler(
                    servicer.GetENBState,
                    request_deserializer=orc8r_dot_protos_dot_common__pb2.Void.FromString,
                    response_serializer=lte_dot_protos_dot_s1ap__service__pb2.EnbStateResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'magma.lte.S1apService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class S1apService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetENBState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.S1apService/GetENBState',
            orc8r_dot_protos_dot_common__pb2.Void.SerializeToString,
            lte_dot_protos_dot_s1ap__service__pb2.EnbStateResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
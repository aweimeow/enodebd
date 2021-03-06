# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from orc8r.protos import common_pb2 as orc8r_dot_protos_dot_common__pb2
from orc8r.protos import metricsd_pb2 as orc8r_dot_protos_dot_metricsd__pb2


class MetricsControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Collect = channel.unary_unary(
                '/magma.orc8r.MetricsController/Collect',
                request_serializer=orc8r_dot_protos_dot_metricsd__pb2.MetricsContainer.SerializeToString,
                response_deserializer=orc8r_dot_protos_dot_common__pb2.Void.FromString,
                )
        self.Push = channel.unary_unary(
                '/magma.orc8r.MetricsController/Push',
                request_serializer=orc8r_dot_protos_dot_metricsd__pb2.PushedMetricsContainer.SerializeToString,
                response_deserializer=orc8r_dot_protos_dot_common__pb2.Void.FromString,
                )


class MetricsControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Collect(self, request, context):
        """Report a collection of metrics from a service
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Push(self, request, context):
        """Push a collection of metrics to metricsd
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MetricsControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Collect': grpc.unary_unary_rpc_method_handler(
                    servicer.Collect,
                    request_deserializer=orc8r_dot_protos_dot_metricsd__pb2.MetricsContainer.FromString,
                    response_serializer=orc8r_dot_protos_dot_common__pb2.Void.SerializeToString,
            ),
            'Push': grpc.unary_unary_rpc_method_handler(
                    servicer.Push,
                    request_deserializer=orc8r_dot_protos_dot_metricsd__pb2.PushedMetricsContainer.FromString,
                    response_serializer=orc8r_dot_protos_dot_common__pb2.Void.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'magma.orc8r.MetricsController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MetricsController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Collect(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.orc8r.MetricsController/Collect',
            orc8r_dot_protos_dot_metricsd__pb2.MetricsContainer.SerializeToString,
            orc8r_dot_protos_dot_common__pb2.Void.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Push(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.orc8r.MetricsController/Push',
            orc8r_dot_protos_dot_metricsd__pb2.PushedMetricsContainer.SerializeToString,
            orc8r_dot_protos_dot_common__pb2.Void.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from orc8r.protos import ctraced_pb2 as orc8r_dot_protos_dot_ctraced__pb2


class CallTraceServiceStub(object):
    """--------------------------------------------------------------------------
    CallTraceService definition (runs on gateway)
    --------------------------------------------------------------------------

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StartCallTrace = channel.unary_unary(
                '/magma.orc8r.CallTraceService/StartCallTrace',
                request_serializer=orc8r_dot_protos_dot_ctraced__pb2.StartTraceRequest.SerializeToString,
                response_deserializer=orc8r_dot_protos_dot_ctraced__pb2.StartTraceResponse.FromString,
                )
        self.EndCallTrace = channel.unary_unary(
                '/magma.orc8r.CallTraceService/EndCallTrace',
                request_serializer=orc8r_dot_protos_dot_ctraced__pb2.EndTraceRequest.SerializeToString,
                response_deserializer=orc8r_dot_protos_dot_ctraced__pb2.EndTraceResponse.FromString,
                )


class CallTraceServiceServicer(object):
    """--------------------------------------------------------------------------
    CallTraceService definition (runs on gateway)
    --------------------------------------------------------------------------

    """

    def StartCallTrace(self, request, context):
        """Start a call trace on the gateway with the specified options.
        Only a single call trace can be active on a gateway at a time.

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EndCallTrace(self, request, context):
        """End the call trace that is currently active on the gateway.

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CallTraceServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StartCallTrace': grpc.unary_unary_rpc_method_handler(
                    servicer.StartCallTrace,
                    request_deserializer=orc8r_dot_protos_dot_ctraced__pb2.StartTraceRequest.FromString,
                    response_serializer=orc8r_dot_protos_dot_ctraced__pb2.StartTraceResponse.SerializeToString,
            ),
            'EndCallTrace': grpc.unary_unary_rpc_method_handler(
                    servicer.EndCallTrace,
                    request_deserializer=orc8r_dot_protos_dot_ctraced__pb2.EndTraceRequest.FromString,
                    response_serializer=orc8r_dot_protos_dot_ctraced__pb2.EndTraceResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'magma.orc8r.CallTraceService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CallTraceService(object):
    """--------------------------------------------------------------------------
    CallTraceService definition (runs on gateway)
    --------------------------------------------------------------------------

    """

    @staticmethod
    def StartCallTrace(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.orc8r.CallTraceService/StartCallTrace',
            orc8r_dot_protos_dot_ctraced__pb2.StartTraceRequest.SerializeToString,
            orc8r_dot_protos_dot_ctraced__pb2.StartTraceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EndCallTrace(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.orc8r.CallTraceService/EndCallTrace',
            orc8r_dot_protos_dot_ctraced__pb2.EndTraceRequest.SerializeToString,
            orc8r_dot_protos_dot_ctraced__pb2.EndTraceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class CallTraceControllerStub(object):
    """--------------------------------------------------------------------------
    CallTraceController definition (runs on cloud)
    --------------------------------------------------------------------------

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ReportEndedCallTrace = channel.unary_unary(
                '/magma.orc8r.CallTraceController/ReportEndedCallTrace',
                request_serializer=orc8r_dot_protos_dot_ctraced__pb2.ReportEndedTraceRequest.SerializeToString,
                response_deserializer=orc8r_dot_protos_dot_ctraced__pb2.ReportEndedTraceResponse.FromString,
                )


class CallTraceControllerServicer(object):
    """--------------------------------------------------------------------------
    CallTraceController definition (runs on cloud)
    --------------------------------------------------------------------------

    """

    def ReportEndedCallTrace(self, request, context):
        """Report that a call trace has ended

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CallTraceControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ReportEndedCallTrace': grpc.unary_unary_rpc_method_handler(
                    servicer.ReportEndedCallTrace,
                    request_deserializer=orc8r_dot_protos_dot_ctraced__pb2.ReportEndedTraceRequest.FromString,
                    response_serializer=orc8r_dot_protos_dot_ctraced__pb2.ReportEndedTraceResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'magma.orc8r.CallTraceController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CallTraceController(object):
    """--------------------------------------------------------------------------
    CallTraceController definition (runs on cloud)
    --------------------------------------------------------------------------

    """

    @staticmethod
    def ReportEndedCallTrace(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.orc8r.CallTraceController/ReportEndedCallTrace',
            orc8r_dot_protos_dot_ctraced__pb2.ReportEndedTraceRequest.SerializeToString,
            orc8r_dot_protos_dot_ctraced__pb2.ReportEndedTraceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

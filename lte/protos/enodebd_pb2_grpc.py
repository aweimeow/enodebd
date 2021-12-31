# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from lte.protos import enodebd_pb2 as lte_dot_protos_dot_enodebd__pb2
from orc8r.protos import common_pb2 as orc8r_dot_protos_dot_common__pb2
from orc8r.protos import service303_pb2 as orc8r_dot_protos_dot_service303__pb2


class EnodebdStub(object):
    """--------------------------------------------------------------------------
    Enodebd service definition.
    --------------------------------------------------------------------------
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetParameter = channel.unary_unary(
                '/magma.lte.Enodebd/GetParameter',
                request_serializer=lte_dot_protos_dot_enodebd__pb2.GetParameterRequest.SerializeToString,
                response_deserializer=lte_dot_protos_dot_enodebd__pb2.GetParameterResponse.FromString,
                )
        self.SetParameter = channel.unary_unary(
                '/magma.lte.Enodebd/SetParameter',
                request_serializer=lte_dot_protos_dot_enodebd__pb2.SetParameterRequest.SerializeToString,
                response_deserializer=orc8r_dot_protos_dot_common__pb2.Void.FromString,
                )
        self.Configure = channel.unary_unary(
                '/magma.lte.Enodebd/Configure',
                request_serializer=lte_dot_protos_dot_enodebd__pb2.EnodebIdentity.SerializeToString,
                response_deserializer=orc8r_dot_protos_dot_common__pb2.Void.FromString,
                )
        self.Reboot = channel.unary_unary(
                '/magma.lte.Enodebd/Reboot',
                request_serializer=lte_dot_protos_dot_enodebd__pb2.EnodebIdentity.SerializeToString,
                response_deserializer=orc8r_dot_protos_dot_common__pb2.Void.FromString,
                )
        self.RebootAll = channel.unary_unary(
                '/magma.lte.Enodebd/RebootAll',
                request_serializer=orc8r_dot_protos_dot_common__pb2.Void.SerializeToString,
                response_deserializer=orc8r_dot_protos_dot_common__pb2.Void.FromString,
                )
        self.GetStatus = channel.unary_unary(
                '/magma.lte.Enodebd/GetStatus',
                request_serializer=orc8r_dot_protos_dot_common__pb2.Void.SerializeToString,
                response_deserializer=orc8r_dot_protos_dot_service303__pb2.ServiceStatus.FromString,
                )
        self.GetAllEnodebStatus = channel.unary_unary(
                '/magma.lte.Enodebd/GetAllEnodebStatus',
                request_serializer=orc8r_dot_protos_dot_common__pb2.Void.SerializeToString,
                response_deserializer=lte_dot_protos_dot_enodebd__pb2.AllEnodebStatus.FromString,
                )
        self.GetEnodebStatus = channel.unary_unary(
                '/magma.lte.Enodebd/GetEnodebStatus',
                request_serializer=lte_dot_protos_dot_enodebd__pb2.EnodebIdentity.SerializeToString,
                response_deserializer=lte_dot_protos_dot_enodebd__pb2.SingleEnodebStatus.FromString,
                )


class EnodebdServicer(object):
    """--------------------------------------------------------------------------
    Enodebd service definition.
    --------------------------------------------------------------------------
    """

    def GetParameter(self, request, context):
        """Sends GetParameterValues message to ENodeB. TR-069 supports multiple
        parameter names per message, but only one is supported here.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetParameter(self, request, context):
        """Sends SetParameterValues message to ENodeB. TR-069 supports multiple
        parameter names per message, but only one is supported here.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Configure(self, request, context):
        """Configure eNodeB based on enodebd config file
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Reboot(self, request, context):
        """Reboot eNodeB
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RebootAll(self, request, context):
        """Reboot every connected eNodeB
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStatus(self, request, context):
        """Get current status
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllEnodebStatus(self, request, context):
        """Get status info for all connected eNodeB devices
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEnodebStatus(self, request, context):
        """Get status info of a single connected eNodeB device
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EnodebdServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetParameter': grpc.unary_unary_rpc_method_handler(
                    servicer.GetParameter,
                    request_deserializer=lte_dot_protos_dot_enodebd__pb2.GetParameterRequest.FromString,
                    response_serializer=lte_dot_protos_dot_enodebd__pb2.GetParameterResponse.SerializeToString,
            ),
            'SetParameter': grpc.unary_unary_rpc_method_handler(
                    servicer.SetParameter,
                    request_deserializer=lte_dot_protos_dot_enodebd__pb2.SetParameterRequest.FromString,
                    response_serializer=orc8r_dot_protos_dot_common__pb2.Void.SerializeToString,
            ),
            'Configure': grpc.unary_unary_rpc_method_handler(
                    servicer.Configure,
                    request_deserializer=lte_dot_protos_dot_enodebd__pb2.EnodebIdentity.FromString,
                    response_serializer=orc8r_dot_protos_dot_common__pb2.Void.SerializeToString,
            ),
            'Reboot': grpc.unary_unary_rpc_method_handler(
                    servicer.Reboot,
                    request_deserializer=lte_dot_protos_dot_enodebd__pb2.EnodebIdentity.FromString,
                    response_serializer=orc8r_dot_protos_dot_common__pb2.Void.SerializeToString,
            ),
            'RebootAll': grpc.unary_unary_rpc_method_handler(
                    servicer.RebootAll,
                    request_deserializer=orc8r_dot_protos_dot_common__pb2.Void.FromString,
                    response_serializer=orc8r_dot_protos_dot_common__pb2.Void.SerializeToString,
            ),
            'GetStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStatus,
                    request_deserializer=orc8r_dot_protos_dot_common__pb2.Void.FromString,
                    response_serializer=orc8r_dot_protos_dot_service303__pb2.ServiceStatus.SerializeToString,
            ),
            'GetAllEnodebStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllEnodebStatus,
                    request_deserializer=orc8r_dot_protos_dot_common__pb2.Void.FromString,
                    response_serializer=lte_dot_protos_dot_enodebd__pb2.AllEnodebStatus.SerializeToString,
            ),
            'GetEnodebStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEnodebStatus,
                    request_deserializer=lte_dot_protos_dot_enodebd__pb2.EnodebIdentity.FromString,
                    response_serializer=lte_dot_protos_dot_enodebd__pb2.SingleEnodebStatus.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'magma.lte.Enodebd', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Enodebd(object):
    """--------------------------------------------------------------------------
    Enodebd service definition.
    --------------------------------------------------------------------------
    """

    @staticmethod
    def GetParameter(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.Enodebd/GetParameter',
            lte_dot_protos_dot_enodebd__pb2.GetParameterRequest.SerializeToString,
            lte_dot_protos_dot_enodebd__pb2.GetParameterResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetParameter(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.Enodebd/SetParameter',
            lte_dot_protos_dot_enodebd__pb2.SetParameterRequest.SerializeToString,
            orc8r_dot_protos_dot_common__pb2.Void.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Configure(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.Enodebd/Configure',
            lte_dot_protos_dot_enodebd__pb2.EnodebIdentity.SerializeToString,
            orc8r_dot_protos_dot_common__pb2.Void.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Reboot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.Enodebd/Reboot',
            lte_dot_protos_dot_enodebd__pb2.EnodebIdentity.SerializeToString,
            orc8r_dot_protos_dot_common__pb2.Void.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RebootAll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.Enodebd/RebootAll',
            orc8r_dot_protos_dot_common__pb2.Void.SerializeToString,
            orc8r_dot_protos_dot_common__pb2.Void.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.Enodebd/GetStatus',
            orc8r_dot_protos_dot_common__pb2.Void.SerializeToString,
            orc8r_dot_protos_dot_service303__pb2.ServiceStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllEnodebStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.Enodebd/GetAllEnodebStatus',
            orc8r_dot_protos_dot_common__pb2.Void.SerializeToString,
            lte_dot_protos_dot_enodebd__pb2.AllEnodebStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetEnodebStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.Enodebd/GetEnodebStatus',
            lte_dot_protos_dot_enodebd__pb2.EnodebIdentity.SerializeToString,
            lte_dot_protos_dot_enodebd__pb2.SingleEnodebStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
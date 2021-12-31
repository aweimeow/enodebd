# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from orc8r.protos import bootstrapper_pb2 as orc8r_dot_protos_dot_bootstrapper__pb2
from orc8r.protos import certifier_pb2 as orc8r_dot_protos_dot_certifier__pb2
from orc8r.protos import identity_pb2 as orc8r_dot_protos_dot_identity__pb2


class BootstrapperStub(object):
    """Note that the security of this service is dependent on TLS to protect
    against MITM and replay attacks
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetChallenge = channel.unary_unary(
                '/magma.orc8r.Bootstrapper/GetChallenge',
                request_serializer=orc8r_dot_protos_dot_identity__pb2.AccessGatewayID.SerializeToString,
                response_deserializer=orc8r_dot_protos_dot_bootstrapper__pb2.Challenge.FromString,
                )
        self.RequestSign = channel.unary_unary(
                '/magma.orc8r.Bootstrapper/RequestSign',
                request_serializer=orc8r_dot_protos_dot_bootstrapper__pb2.Response.SerializeToString,
                response_deserializer=orc8r_dot_protos_dot_certifier__pb2.Certificate.FromString,
                )


class BootstrapperServicer(object):
    """Note that the security of this service is dependent on TLS to protect
    against MITM and replay attacks
    """

    def GetChallenge(self, request, context):
        """get the challange for gateway specified in hw_id (AccessGatewayID)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RequestSign(self, request, context):
        """send back response and csr for signing
        Returns signed certificate.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BootstrapperServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetChallenge': grpc.unary_unary_rpc_method_handler(
                    servicer.GetChallenge,
                    request_deserializer=orc8r_dot_protos_dot_identity__pb2.AccessGatewayID.FromString,
                    response_serializer=orc8r_dot_protos_dot_bootstrapper__pb2.Challenge.SerializeToString,
            ),
            'RequestSign': grpc.unary_unary_rpc_method_handler(
                    servicer.RequestSign,
                    request_deserializer=orc8r_dot_protos_dot_bootstrapper__pb2.Response.FromString,
                    response_serializer=orc8r_dot_protos_dot_certifier__pb2.Certificate.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'magma.orc8r.Bootstrapper', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Bootstrapper(object):
    """Note that the security of this service is dependent on TLS to protect
    against MITM and replay attacks
    """

    @staticmethod
    def GetChallenge(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.orc8r.Bootstrapper/GetChallenge',
            orc8r_dot_protos_dot_identity__pb2.AccessGatewayID.SerializeToString,
            orc8r_dot_protos_dot_bootstrapper__pb2.Challenge.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RequestSign(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.orc8r.Bootstrapper/RequestSign',
            orc8r_dot_protos_dot_bootstrapper__pb2.Response.SerializeToString,
            orc8r_dot_protos_dot_certifier__pb2.Certificate.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

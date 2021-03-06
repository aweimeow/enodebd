# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from lte.protos import subscriberauth_pb2 as lte_dot_protos_dot_subscriberauth__pb2


class M5GSubscriberAuthenticationStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.M5GAuthenticationInformation = channel.unary_unary(
                '/magma.lte.M5GSubscriberAuthentication/M5GAuthenticationInformation',
                request_serializer=lte_dot_protos_dot_subscriberauth__pb2.M5GAuthenticationInformationRequest.SerializeToString,
                response_deserializer=lte_dot_protos_dot_subscriberauth__pb2.M5GAuthenticationInformationAnswer.FromString,
                )


class M5GSubscriberAuthenticationServicer(object):
    """Missing associated documentation comment in .proto file."""

    def M5GAuthenticationInformation(self, request, context):
        """Authentication-Information (Code 318)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_M5GSubscriberAuthenticationServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'M5GAuthenticationInformation': grpc.unary_unary_rpc_method_handler(
                    servicer.M5GAuthenticationInformation,
                    request_deserializer=lte_dot_protos_dot_subscriberauth__pb2.M5GAuthenticationInformationRequest.FromString,
                    response_serializer=lte_dot_protos_dot_subscriberauth__pb2.M5GAuthenticationInformationAnswer.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'magma.lte.M5GSubscriberAuthentication', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class M5GSubscriberAuthentication(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def M5GAuthenticationInformation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.M5GSubscriberAuthentication/M5GAuthenticationInformation',
            lte_dot_protos_dot_subscriberauth__pb2.M5GAuthenticationInformationRequest.SerializeToString,
            lte_dot_protos_dot_subscriberauth__pb2.M5GAuthenticationInformationAnswer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

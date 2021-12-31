# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from lte.protos import sctpd_pb2 as lte_dot_protos_dot_sctpd__pb2


class SctpdDownlinkStub(object):
    """facilitates MME -> eNB messages
    - server lives in sctpd
    - sctp task calls in response to itti messages
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Init = channel.unary_unary(
                '/magma.sctpd.SctpdDownlink/Init',
                request_serializer=lte_dot_protos_dot_sctpd__pb2.InitReq.SerializeToString,
                response_deserializer=lte_dot_protos_dot_sctpd__pb2.InitRes.FromString,
                )
        self.SendDl = channel.unary_unary(
                '/magma.sctpd.SctpdDownlink/SendDl',
                request_serializer=lte_dot_protos_dot_sctpd__pb2.SendDlReq.SerializeToString,
                response_deserializer=lte_dot_protos_dot_sctpd__pb2.SendDlRes.FromString,
                )


class SctpdDownlinkServicer(object):
    """facilitates MME -> eNB messages
    - server lives in sctpd
    - sctp task calls in response to itti messages
    """

    def Init(self, request, context):
        """Init - initialize sctp connection according to InitReq
        @param InitReq request specifying desired sctp configuration
        @return InitRes response w/ init success status
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendDl(self, request, context):
        """SendDl - send a downlink packet to eNB
        @param SendDlReq request specifying packet data and destination
        @return SendDlRes response w/ send success status
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SctpdDownlinkServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Init': grpc.unary_unary_rpc_method_handler(
                    servicer.Init,
                    request_deserializer=lte_dot_protos_dot_sctpd__pb2.InitReq.FromString,
                    response_serializer=lte_dot_protos_dot_sctpd__pb2.InitRes.SerializeToString,
            ),
            'SendDl': grpc.unary_unary_rpc_method_handler(
                    servicer.SendDl,
                    request_deserializer=lte_dot_protos_dot_sctpd__pb2.SendDlReq.FromString,
                    response_serializer=lte_dot_protos_dot_sctpd__pb2.SendDlRes.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'magma.sctpd.SctpdDownlink', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SctpdDownlink(object):
    """facilitates MME -> eNB messages
    - server lives in sctpd
    - sctp task calls in response to itti messages
    """

    @staticmethod
    def Init(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.sctpd.SctpdDownlink/Init',
            lte_dot_protos_dot_sctpd__pb2.InitReq.SerializeToString,
            lte_dot_protos_dot_sctpd__pb2.InitRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendDl(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.sctpd.SctpdDownlink/SendDl',
            lte_dot_protos_dot_sctpd__pb2.SendDlReq.SerializeToString,
            lte_dot_protos_dot_sctpd__pb2.SendDlRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class SctpdUplinkStub(object):
    """facilitates eNB -> MME messages
    - server lives in MME
    - sctpd calls from sctp listener loop
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendUl = channel.unary_unary(
                '/magma.sctpd.SctpdUplink/SendUl',
                request_serializer=lte_dot_protos_dot_sctpd__pb2.SendUlReq.SerializeToString,
                response_deserializer=lte_dot_protos_dot_sctpd__pb2.SendUlRes.FromString,
                )
        self.NewAssoc = channel.unary_unary(
                '/magma.sctpd.SctpdUplink/NewAssoc',
                request_serializer=lte_dot_protos_dot_sctpd__pb2.NewAssocReq.SerializeToString,
                response_deserializer=lte_dot_protos_dot_sctpd__pb2.NewAssocRes.FromString,
                )
        self.CloseAssoc = channel.unary_unary(
                '/magma.sctpd.SctpdUplink/CloseAssoc',
                request_serializer=lte_dot_protos_dot_sctpd__pb2.CloseAssocReq.SerializeToString,
                response_deserializer=lte_dot_protos_dot_sctpd__pb2.CloseAssocRes.FromString,
                )


class SctpdUplinkServicer(object):
    """facilitates eNB -> MME messages
    - server lives in MME
    - sctpd calls from sctp listener loop
    """

    def SendUl(self, request, context):
        """SendUl - send an uplink packet to MME
        @param SendUlReq request specifying packet data and destination
        @return SendUlRes void response object
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NewAssoc(self, request, context):
        """NewAssoc - notify MME of new eNB association
        @param NewAssocReq request specifying new association's information
        @return NewAssocRes void response object
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CloseAssoc(self, request, context):
        """CloseAssoc - notify MME of closing/resetting eNB association
        @param CloseAssocReq request specifying closing association and close type
        @return CloseAssocRes void response object
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SctpdUplinkServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendUl': grpc.unary_unary_rpc_method_handler(
                    servicer.SendUl,
                    request_deserializer=lte_dot_protos_dot_sctpd__pb2.SendUlReq.FromString,
                    response_serializer=lte_dot_protos_dot_sctpd__pb2.SendUlRes.SerializeToString,
            ),
            'NewAssoc': grpc.unary_unary_rpc_method_handler(
                    servicer.NewAssoc,
                    request_deserializer=lte_dot_protos_dot_sctpd__pb2.NewAssocReq.FromString,
                    response_serializer=lte_dot_protos_dot_sctpd__pb2.NewAssocRes.SerializeToString,
            ),
            'CloseAssoc': grpc.unary_unary_rpc_method_handler(
                    servicer.CloseAssoc,
                    request_deserializer=lte_dot_protos_dot_sctpd__pb2.CloseAssocReq.FromString,
                    response_serializer=lte_dot_protos_dot_sctpd__pb2.CloseAssocRes.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'magma.sctpd.SctpdUplink', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SctpdUplink(object):
    """facilitates eNB -> MME messages
    - server lives in MME
    - sctpd calls from sctp listener loop
    """

    @staticmethod
    def SendUl(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.sctpd.SctpdUplink/SendUl',
            lte_dot_protos_dot_sctpd__pb2.SendUlReq.SerializeToString,
            lte_dot_protos_dot_sctpd__pb2.SendUlRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NewAssoc(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.sctpd.SctpdUplink/NewAssoc',
            lte_dot_protos_dot_sctpd__pb2.NewAssocReq.SerializeToString,
            lte_dot_protos_dot_sctpd__pb2.NewAssocRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CloseAssoc(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.sctpd.SctpdUplink/CloseAssoc',
            lte_dot_protos_dot_sctpd__pb2.CloseAssocReq.SerializeToString,
            lte_dot_protos_dot_sctpd__pb2.CloseAssocRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from lte.protos import policydb_pb2 as lte_dot_protos_dot_policydb__pb2
from orc8r.protos import common_pb2 as orc8r_dot_protos_dot_common__pb2


class PolicyAssignmentControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.EnableStaticRules = channel.unary_unary(
                '/magma.lte.PolicyAssignmentController/EnableStaticRules',
                request_serializer=lte_dot_protos_dot_policydb__pb2.EnableStaticRuleRequest.SerializeToString,
                response_deserializer=orc8r_dot_protos_dot_common__pb2.Void.FromString,
                )
        self.DisableStaticRules = channel.unary_unary(
                '/magma.lte.PolicyAssignmentController/DisableStaticRules',
                request_serializer=lte_dot_protos_dot_policydb__pb2.DisableStaticRuleRequest.SerializeToString,
                response_deserializer=orc8r_dot_protos_dot_common__pb2.Void.FromString,
                )


class PolicyAssignmentControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def EnableStaticRules(self, request, context):
        """Associate the static rule with the IMSI

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DisableStaticRules(self, request, context):
        """Unassociate the static rule with the IMSI

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PolicyAssignmentControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'EnableStaticRules': grpc.unary_unary_rpc_method_handler(
                    servicer.EnableStaticRules,
                    request_deserializer=lte_dot_protos_dot_policydb__pb2.EnableStaticRuleRequest.FromString,
                    response_serializer=orc8r_dot_protos_dot_common__pb2.Void.SerializeToString,
            ),
            'DisableStaticRules': grpc.unary_unary_rpc_method_handler(
                    servicer.DisableStaticRules,
                    request_deserializer=lte_dot_protos_dot_policydb__pb2.DisableStaticRuleRequest.FromString,
                    response_serializer=orc8r_dot_protos_dot_common__pb2.Void.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'magma.lte.PolicyAssignmentController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PolicyAssignmentController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def EnableStaticRules(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.PolicyAssignmentController/EnableStaticRules',
            lte_dot_protos_dot_policydb__pb2.EnableStaticRuleRequest.SerializeToString,
            orc8r_dot_protos_dot_common__pb2.Void.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DisableStaticRules(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.PolicyAssignmentController/DisableStaticRules',
            lte_dot_protos_dot_policydb__pb2.DisableStaticRuleRequest.SerializeToString,
            orc8r_dot_protos_dot_common__pb2.Void.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class PolicyDBStub(object):
    """--------------------------------------------------------------------------
    PolicyDB service definition
    --------------------------------------------------------------------------
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.EnableStaticRules = channel.unary_unary(
                '/magma.lte.PolicyDB/EnableStaticRules',
                request_serializer=lte_dot_protos_dot_policydb__pb2.EnableStaticRuleRequest.SerializeToString,
                response_deserializer=orc8r_dot_protos_dot_common__pb2.Void.FromString,
                )
        self.DisableStaticRules = channel.unary_unary(
                '/magma.lte.PolicyDB/DisableStaticRules',
                request_serializer=lte_dot_protos_dot_policydb__pb2.DisableStaticRuleRequest.SerializeToString,
                response_deserializer=orc8r_dot_protos_dot_common__pb2.Void.FromString,
                )


class PolicyDBServicer(object):
    """--------------------------------------------------------------------------
    PolicyDB service definition
    --------------------------------------------------------------------------
    """

    def EnableStaticRules(self, request, context):
        """Immediately install the static policy for the IMSI
        Also unassociate the static rule with the IMSI on orc8r

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DisableStaticRules(self, request, context):
        """Immediately uninstall the static policy for the IMSI
        Also unassociate the static rule with the IMSI on orc8r

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PolicyDBServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'EnableStaticRules': grpc.unary_unary_rpc_method_handler(
                    servicer.EnableStaticRules,
                    request_deserializer=lte_dot_protos_dot_policydb__pb2.EnableStaticRuleRequest.FromString,
                    response_serializer=orc8r_dot_protos_dot_common__pb2.Void.SerializeToString,
            ),
            'DisableStaticRules': grpc.unary_unary_rpc_method_handler(
                    servicer.DisableStaticRules,
                    request_deserializer=lte_dot_protos_dot_policydb__pb2.DisableStaticRuleRequest.FromString,
                    response_serializer=orc8r_dot_protos_dot_common__pb2.Void.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'magma.lte.PolicyDB', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PolicyDB(object):
    """--------------------------------------------------------------------------
    PolicyDB service definition
    --------------------------------------------------------------------------
    """

    @staticmethod
    def EnableStaticRules(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.PolicyDB/EnableStaticRules',
            lte_dot_protos_dot_policydb__pb2.EnableStaticRuleRequest.SerializeToString,
            orc8r_dot_protos_dot_common__pb2.Void.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DisableStaticRules(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.PolicyDB/DisableStaticRules',
            lte_dot_protos_dot_policydb__pb2.DisableStaticRuleRequest.SerializeToString,
            orc8r_dot_protos_dot_common__pb2.Void.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
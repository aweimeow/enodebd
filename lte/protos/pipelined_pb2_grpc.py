# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from lte.protos import pipelined_pb2 as lte_dot_protos_dot_pipelined__pb2
from lte.protos import session_manager_pb2 as lte_dot_protos_dot_session__manager__pb2
from orc8r.protos import common_pb2 as orc8r_dot_protos_dot_common__pb2


class PipelinedStub(object):
    """--------------------------------------------------------------------------
    Pipelined gateway RPC service
    --------------------------------------------------------------------------
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetupDefaultControllers = channel.unary_unary(
                '/magma.lte.Pipelined/SetupDefaultControllers',
                request_serializer=lte_dot_protos_dot_pipelined__pb2.SetupDefaultRequest.SerializeToString,
                response_deserializer=lte_dot_protos_dot_pipelined__pb2.SetupFlowsResult.FromString,
                )
        self.SetSMFSessions = channel.unary_unary(
                '/magma.lte.Pipelined/SetSMFSessions',
                request_serializer=lte_dot_protos_dot_pipelined__pb2.SessionSet.SerializeToString,
                response_deserializer=lte_dot_protos_dot_pipelined__pb2.UPFSessionContextState.FromString,
                )
        self.SetupPolicyFlows = channel.unary_unary(
                '/magma.lte.Pipelined/SetupPolicyFlows',
                request_serializer=lte_dot_protos_dot_pipelined__pb2.SetupPolicyRequest.SerializeToString,
                response_deserializer=lte_dot_protos_dot_pipelined__pb2.SetupFlowsResult.FromString,
                )
        self.ActivateFlows = channel.unary_unary(
                '/magma.lte.Pipelined/ActivateFlows',
                request_serializer=lte_dot_protos_dot_pipelined__pb2.ActivateFlowsRequest.SerializeToString,
                response_deserializer=lte_dot_protos_dot_pipelined__pb2.ActivateFlowsResult.FromString,
                )
        self.DeactivateFlows = channel.unary_unary(
                '/magma.lte.Pipelined/DeactivateFlows',
                request_serializer=lte_dot_protos_dot_pipelined__pb2.DeactivateFlowsRequest.SerializeToString,
                response_deserializer=lte_dot_protos_dot_pipelined__pb2.DeactivateFlowsResult.FromString,
                )
        self.GetPolicyUsage = channel.unary_unary(
                '/magma.lte.Pipelined/GetPolicyUsage',
                request_serializer=orc8r_dot_protos_dot_common__pb2.Void.SerializeToString,
                response_deserializer=lte_dot_protos_dot_session__manager__pb2.RuleRecordTable.FromString,
                )
        self.GetStats = channel.unary_unary(
                '/magma.lte.Pipelined/GetStats',
                request_serializer=lte_dot_protos_dot_pipelined__pb2.GetStatsRequest.SerializeToString,
                response_deserializer=lte_dot_protos_dot_session__manager__pb2.RuleRecordTable.FromString,
                )
        self.CreateFlow = channel.unary_unary(
                '/magma.lte.Pipelined/CreateFlow',
                request_serializer=lte_dot_protos_dot_pipelined__pb2.FlowRequest.SerializeToString,
                response_deserializer=lte_dot_protos_dot_pipelined__pb2.FlowResponse.FromString,
                )
        self.RemoveFlow = channel.unary_unary(
                '/magma.lte.Pipelined/RemoveFlow',
                request_serializer=lte_dot_protos_dot_pipelined__pb2.FlowRequest.SerializeToString,
                response_deserializer=lte_dot_protos_dot_pipelined__pb2.FlowResponse.FromString,
                )
        self.UpdateFlowStats = channel.unary_unary(
                '/magma.lte.Pipelined/UpdateFlowStats',
                request_serializer=lte_dot_protos_dot_pipelined__pb2.FlowRequest.SerializeToString,
                response_deserializer=lte_dot_protos_dot_pipelined__pb2.FlowResponse.FromString,
                )
        self.SetupQuotaFlows = channel.unary_unary(
                '/magma.lte.Pipelined/SetupQuotaFlows',
                request_serializer=lte_dot_protos_dot_pipelined__pb2.SetupQuotaRequest.SerializeToString,
                response_deserializer=lte_dot_protos_dot_pipelined__pb2.SetupFlowsResult.FromString,
                )
        self.UpdateSubscriberQuotaState = channel.unary_unary(
                '/magma.lte.Pipelined/UpdateSubscriberQuotaState',
                request_serializer=lte_dot_protos_dot_pipelined__pb2.UpdateSubscriberQuotaStateRequest.SerializeToString,
                response_deserializer=lte_dot_protos_dot_pipelined__pb2.FlowResponse.FromString,
                )
        self.SetupUEMacFlows = channel.unary_unary(
                '/magma.lte.Pipelined/SetupUEMacFlows',
                request_serializer=lte_dot_protos_dot_pipelined__pb2.SetupUEMacRequest.SerializeToString,
                response_deserializer=lte_dot_protos_dot_pipelined__pb2.SetupFlowsResult.FromString,
                )
        self.AddUEMacFlow = channel.unary_unary(
                '/magma.lte.Pipelined/AddUEMacFlow',
                request_serializer=lte_dot_protos_dot_pipelined__pb2.UEMacFlowRequest.SerializeToString,
                response_deserializer=lte_dot_protos_dot_pipelined__pb2.FlowResponse.FromString,
                )
        self.DeleteUEMacFlow = channel.unary_unary(
                '/magma.lte.Pipelined/DeleteUEMacFlow',
                request_serializer=lte_dot_protos_dot_pipelined__pb2.UEMacFlowRequest.SerializeToString,
                response_deserializer=lte_dot_protos_dot_pipelined__pb2.FlowResponse.FromString,
                )
        self.UpdateIPFIXFlow = channel.unary_unary(
                '/magma.lte.Pipelined/UpdateIPFIXFlow',
                request_serializer=lte_dot_protos_dot_pipelined__pb2.UEMacFlowRequest.SerializeToString,
                response_deserializer=lte_dot_protos_dot_pipelined__pb2.FlowResponse.FromString,
                )
        self.GetAllTableAssignments = channel.unary_unary(
                '/magma.lte.Pipelined/GetAllTableAssignments',
                request_serializer=orc8r_dot_protos_dot_common__pb2.Void.SerializeToString,
                response_deserializer=lte_dot_protos_dot_pipelined__pb2.AllTableAssignments.FromString,
                )
        self.UpdateUEState = channel.unary_unary(
                '/magma.lte.Pipelined/UpdateUEState',
                request_serializer=lte_dot_protos_dot_pipelined__pb2.UESessionSet.SerializeToString,
                response_deserializer=lte_dot_protos_dot_pipelined__pb2.UESessionContextResponse.FromString,
                )


class PipelinedServicer(object):
    """--------------------------------------------------------------------------
    Pipelined gateway RPC service
    --------------------------------------------------------------------------
    """

    def SetupDefaultControllers(self, request, context):
        """-----------------
        General setup rpc
        -----------------

        Setup pipelined basic controllers
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetSMFSessions(self, request, context):
        """------------
        Smf to Upf rpc
        ------------

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetupPolicyFlows(self, request, context):
        """----------------
        Enforcement App:
        ----------------

        Setup flows for subscribers (used on restarts)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ActivateFlows(self, request, context):
        """Activate flows for a subscriber based on predefined flow templates
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeactivateFlows(self, request, context):
        """Deactivate flows for a subscriber
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPolicyUsage(self, request, context):
        """Get policy usage stats
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStats(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateFlow(self, request, context):
        """--------
        DPI App:
        --------

        Add new dpi flow
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveFlow(self, request, context):
        """Remove dpi flow
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateFlowStats(self, request, context):
        """Update flow stats
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetupQuotaFlows(self, request, context):
        """----------------
        Quota Check App:
        ----------------

        Setup subscribers flows (used on restarts)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateSubscriberQuotaState(self, request, context):
        """Synchronize subscribers quota check flows
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetupUEMacFlows(self, request, context):
        """-----------
        UE MAC App:
        -----------

        Setup subscribers flows (used on restarts)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddUEMacFlow(self, request, context):
        """Add a flow for a subscriber by matching the provided UE MAC address
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteUEMacFlow(self, request, context):
        """Delete a flow for a subscriber by matching the provided UE MAC address
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateIPFIXFlow(self, request, context):
        """-----------
        IPFIX App:
        -----------

        Update subscriber IPFIX flows
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllTableAssignments(self, request, context):
        """--------
        Debugging:
        --------

        Get the flow table assignment for all apps ordered by main table number
        and name
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateUEState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PipelinedServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SetupDefaultControllers': grpc.unary_unary_rpc_method_handler(
                    servicer.SetupDefaultControllers,
                    request_deserializer=lte_dot_protos_dot_pipelined__pb2.SetupDefaultRequest.FromString,
                    response_serializer=lte_dot_protos_dot_pipelined__pb2.SetupFlowsResult.SerializeToString,
            ),
            'SetSMFSessions': grpc.unary_unary_rpc_method_handler(
                    servicer.SetSMFSessions,
                    request_deserializer=lte_dot_protos_dot_pipelined__pb2.SessionSet.FromString,
                    response_serializer=lte_dot_protos_dot_pipelined__pb2.UPFSessionContextState.SerializeToString,
            ),
            'SetupPolicyFlows': grpc.unary_unary_rpc_method_handler(
                    servicer.SetupPolicyFlows,
                    request_deserializer=lte_dot_protos_dot_pipelined__pb2.SetupPolicyRequest.FromString,
                    response_serializer=lte_dot_protos_dot_pipelined__pb2.SetupFlowsResult.SerializeToString,
            ),
            'ActivateFlows': grpc.unary_unary_rpc_method_handler(
                    servicer.ActivateFlows,
                    request_deserializer=lte_dot_protos_dot_pipelined__pb2.ActivateFlowsRequest.FromString,
                    response_serializer=lte_dot_protos_dot_pipelined__pb2.ActivateFlowsResult.SerializeToString,
            ),
            'DeactivateFlows': grpc.unary_unary_rpc_method_handler(
                    servicer.DeactivateFlows,
                    request_deserializer=lte_dot_protos_dot_pipelined__pb2.DeactivateFlowsRequest.FromString,
                    response_serializer=lte_dot_protos_dot_pipelined__pb2.DeactivateFlowsResult.SerializeToString,
            ),
            'GetPolicyUsage': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPolicyUsage,
                    request_deserializer=orc8r_dot_protos_dot_common__pb2.Void.FromString,
                    response_serializer=lte_dot_protos_dot_session__manager__pb2.RuleRecordTable.SerializeToString,
            ),
            'GetStats': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStats,
                    request_deserializer=lte_dot_protos_dot_pipelined__pb2.GetStatsRequest.FromString,
                    response_serializer=lte_dot_protos_dot_session__manager__pb2.RuleRecordTable.SerializeToString,
            ),
            'CreateFlow': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateFlow,
                    request_deserializer=lte_dot_protos_dot_pipelined__pb2.FlowRequest.FromString,
                    response_serializer=lte_dot_protos_dot_pipelined__pb2.FlowResponse.SerializeToString,
            ),
            'RemoveFlow': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveFlow,
                    request_deserializer=lte_dot_protos_dot_pipelined__pb2.FlowRequest.FromString,
                    response_serializer=lte_dot_protos_dot_pipelined__pb2.FlowResponse.SerializeToString,
            ),
            'UpdateFlowStats': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateFlowStats,
                    request_deserializer=lte_dot_protos_dot_pipelined__pb2.FlowRequest.FromString,
                    response_serializer=lte_dot_protos_dot_pipelined__pb2.FlowResponse.SerializeToString,
            ),
            'SetupQuotaFlows': grpc.unary_unary_rpc_method_handler(
                    servicer.SetupQuotaFlows,
                    request_deserializer=lte_dot_protos_dot_pipelined__pb2.SetupQuotaRequest.FromString,
                    response_serializer=lte_dot_protos_dot_pipelined__pb2.SetupFlowsResult.SerializeToString,
            ),
            'UpdateSubscriberQuotaState': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateSubscriberQuotaState,
                    request_deserializer=lte_dot_protos_dot_pipelined__pb2.UpdateSubscriberQuotaStateRequest.FromString,
                    response_serializer=lte_dot_protos_dot_pipelined__pb2.FlowResponse.SerializeToString,
            ),
            'SetupUEMacFlows': grpc.unary_unary_rpc_method_handler(
                    servicer.SetupUEMacFlows,
                    request_deserializer=lte_dot_protos_dot_pipelined__pb2.SetupUEMacRequest.FromString,
                    response_serializer=lte_dot_protos_dot_pipelined__pb2.SetupFlowsResult.SerializeToString,
            ),
            'AddUEMacFlow': grpc.unary_unary_rpc_method_handler(
                    servicer.AddUEMacFlow,
                    request_deserializer=lte_dot_protos_dot_pipelined__pb2.UEMacFlowRequest.FromString,
                    response_serializer=lte_dot_protos_dot_pipelined__pb2.FlowResponse.SerializeToString,
            ),
            'DeleteUEMacFlow': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteUEMacFlow,
                    request_deserializer=lte_dot_protos_dot_pipelined__pb2.UEMacFlowRequest.FromString,
                    response_serializer=lte_dot_protos_dot_pipelined__pb2.FlowResponse.SerializeToString,
            ),
            'UpdateIPFIXFlow': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateIPFIXFlow,
                    request_deserializer=lte_dot_protos_dot_pipelined__pb2.UEMacFlowRequest.FromString,
                    response_serializer=lte_dot_protos_dot_pipelined__pb2.FlowResponse.SerializeToString,
            ),
            'GetAllTableAssignments': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllTableAssignments,
                    request_deserializer=orc8r_dot_protos_dot_common__pb2.Void.FromString,
                    response_serializer=lte_dot_protos_dot_pipelined__pb2.AllTableAssignments.SerializeToString,
            ),
            'UpdateUEState': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateUEState,
                    request_deserializer=lte_dot_protos_dot_pipelined__pb2.UESessionSet.FromString,
                    response_serializer=lte_dot_protos_dot_pipelined__pb2.UESessionContextResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'magma.lte.Pipelined', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Pipelined(object):
    """--------------------------------------------------------------------------
    Pipelined gateway RPC service
    --------------------------------------------------------------------------
    """

    @staticmethod
    def SetupDefaultControllers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.Pipelined/SetupDefaultControllers',
            lte_dot_protos_dot_pipelined__pb2.SetupDefaultRequest.SerializeToString,
            lte_dot_protos_dot_pipelined__pb2.SetupFlowsResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetSMFSessions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.Pipelined/SetSMFSessions',
            lte_dot_protos_dot_pipelined__pb2.SessionSet.SerializeToString,
            lte_dot_protos_dot_pipelined__pb2.UPFSessionContextState.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetupPolicyFlows(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.Pipelined/SetupPolicyFlows',
            lte_dot_protos_dot_pipelined__pb2.SetupPolicyRequest.SerializeToString,
            lte_dot_protos_dot_pipelined__pb2.SetupFlowsResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ActivateFlows(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.Pipelined/ActivateFlows',
            lte_dot_protos_dot_pipelined__pb2.ActivateFlowsRequest.SerializeToString,
            lte_dot_protos_dot_pipelined__pb2.ActivateFlowsResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeactivateFlows(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.Pipelined/DeactivateFlows',
            lte_dot_protos_dot_pipelined__pb2.DeactivateFlowsRequest.SerializeToString,
            lte_dot_protos_dot_pipelined__pb2.DeactivateFlowsResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPolicyUsage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.Pipelined/GetPolicyUsage',
            orc8r_dot_protos_dot_common__pb2.Void.SerializeToString,
            lte_dot_protos_dot_session__manager__pb2.RuleRecordTable.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStats(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.Pipelined/GetStats',
            lte_dot_protos_dot_pipelined__pb2.GetStatsRequest.SerializeToString,
            lte_dot_protos_dot_session__manager__pb2.RuleRecordTable.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateFlow(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.Pipelined/CreateFlow',
            lte_dot_protos_dot_pipelined__pb2.FlowRequest.SerializeToString,
            lte_dot_protos_dot_pipelined__pb2.FlowResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveFlow(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.Pipelined/RemoveFlow',
            lte_dot_protos_dot_pipelined__pb2.FlowRequest.SerializeToString,
            lte_dot_protos_dot_pipelined__pb2.FlowResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateFlowStats(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.Pipelined/UpdateFlowStats',
            lte_dot_protos_dot_pipelined__pb2.FlowRequest.SerializeToString,
            lte_dot_protos_dot_pipelined__pb2.FlowResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetupQuotaFlows(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.Pipelined/SetupQuotaFlows',
            lte_dot_protos_dot_pipelined__pb2.SetupQuotaRequest.SerializeToString,
            lte_dot_protos_dot_pipelined__pb2.SetupFlowsResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateSubscriberQuotaState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.Pipelined/UpdateSubscriberQuotaState',
            lte_dot_protos_dot_pipelined__pb2.UpdateSubscriberQuotaStateRequest.SerializeToString,
            lte_dot_protos_dot_pipelined__pb2.FlowResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetupUEMacFlows(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.Pipelined/SetupUEMacFlows',
            lte_dot_protos_dot_pipelined__pb2.SetupUEMacRequest.SerializeToString,
            lte_dot_protos_dot_pipelined__pb2.SetupFlowsResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddUEMacFlow(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.Pipelined/AddUEMacFlow',
            lte_dot_protos_dot_pipelined__pb2.UEMacFlowRequest.SerializeToString,
            lte_dot_protos_dot_pipelined__pb2.FlowResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteUEMacFlow(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.Pipelined/DeleteUEMacFlow',
            lte_dot_protos_dot_pipelined__pb2.UEMacFlowRequest.SerializeToString,
            lte_dot_protos_dot_pipelined__pb2.FlowResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateIPFIXFlow(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.Pipelined/UpdateIPFIXFlow',
            lte_dot_protos_dot_pipelined__pb2.UEMacFlowRequest.SerializeToString,
            lte_dot_protos_dot_pipelined__pb2.FlowResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllTableAssignments(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.Pipelined/GetAllTableAssignments',
            orc8r_dot_protos_dot_common__pb2.Void.SerializeToString,
            lte_dot_protos_dot_pipelined__pb2.AllTableAssignments.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateUEState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.Pipelined/UpdateUEState',
            lte_dot_protos_dot_pipelined__pb2.UESessionSet.SerializeToString,
            lte_dot_protos_dot_pipelined__pb2.UESessionContextResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

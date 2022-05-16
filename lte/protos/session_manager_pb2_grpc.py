# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from lte.protos import session_manager_pb2 as lte_dot_protos_dot_session__manager__pb2
from orc8r.protos import common_pb2 as orc8r_dot_protos_dot_common__pb2


class LocalSessionManagerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ReportRuleStats = channel.unary_unary(
                '/magma.lte.LocalSessionManager/ReportRuleStats',
                request_serializer=lte_dot_protos_dot_session__manager__pb2.RuleRecordTable.SerializeToString,
                response_deserializer=orc8r_dot_protos_dot_common__pb2.Void.FromString,
                )
        self.CreateSession = channel.unary_unary(
                '/magma.lte.LocalSessionManager/CreateSession',
                request_serializer=lte_dot_protos_dot_session__manager__pb2.LocalCreateSessionRequest.SerializeToString,
                response_deserializer=lte_dot_protos_dot_session__manager__pb2.LocalCreateSessionResponse.FromString,
                )
        self.EndSession = channel.unary_unary(
                '/magma.lte.LocalSessionManager/EndSession',
                request_serializer=lte_dot_protos_dot_session__manager__pb2.LocalEndSessionRequest.SerializeToString,
                response_deserializer=lte_dot_protos_dot_session__manager__pb2.LocalEndSessionResponse.FromString,
                )
        self.BindPolicy2Bearer = channel.unary_unary(
                '/magma.lte.LocalSessionManager/BindPolicy2Bearer',
                request_serializer=lte_dot_protos_dot_session__manager__pb2.PolicyBearerBindingRequest.SerializeToString,
                response_deserializer=lte_dot_protos_dot_session__manager__pb2.PolicyBearerBindingResponse.FromString,
                )
        self.SetSessionRules = channel.unary_unary(
                '/magma.lte.LocalSessionManager/SetSessionRules',
                request_serializer=lte_dot_protos_dot_session__manager__pb2.SessionRules.SerializeToString,
                response_deserializer=orc8r_dot_protos_dot_common__pb2.Void.FromString,
                )
        self.UpdateTunnelIds = channel.unary_unary(
                '/magma.lte.LocalSessionManager/UpdateTunnelIds',
                request_serializer=lte_dot_protos_dot_session__manager__pb2.UpdateTunnelIdsRequest.SerializeToString,
                response_deserializer=lte_dot_protos_dot_session__manager__pb2.UpdateTunnelIdsResponse.FromString,
                )


class LocalSessionManagerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ReportRuleStats(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EndSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BindPolicy2Bearer(self, request, context):
        """A response to CreateBearer request defined in spgw service. Sends a mapping of dedicated bearer ID <-> policy.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetSessionRules(self, request, context):
        """A set interface of subscribers -> currently active rules
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateTunnelIds(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LocalSessionManagerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ReportRuleStats': grpc.unary_unary_rpc_method_handler(
                    servicer.ReportRuleStats,
                    request_deserializer=lte_dot_protos_dot_session__manager__pb2.RuleRecordTable.FromString,
                    response_serializer=orc8r_dot_protos_dot_common__pb2.Void.SerializeToString,
            ),
            'CreateSession': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateSession,
                    request_deserializer=lte_dot_protos_dot_session__manager__pb2.LocalCreateSessionRequest.FromString,
                    response_serializer=lte_dot_protos_dot_session__manager__pb2.LocalCreateSessionResponse.SerializeToString,
            ),
            'EndSession': grpc.unary_unary_rpc_method_handler(
                    servicer.EndSession,
                    request_deserializer=lte_dot_protos_dot_session__manager__pb2.LocalEndSessionRequest.FromString,
                    response_serializer=lte_dot_protos_dot_session__manager__pb2.LocalEndSessionResponse.SerializeToString,
            ),
            'BindPolicy2Bearer': grpc.unary_unary_rpc_method_handler(
                    servicer.BindPolicy2Bearer,
                    request_deserializer=lte_dot_protos_dot_session__manager__pb2.PolicyBearerBindingRequest.FromString,
                    response_serializer=lte_dot_protos_dot_session__manager__pb2.PolicyBearerBindingResponse.SerializeToString,
            ),
            'SetSessionRules': grpc.unary_unary_rpc_method_handler(
                    servicer.SetSessionRules,
                    request_deserializer=lte_dot_protos_dot_session__manager__pb2.SessionRules.FromString,
                    response_serializer=orc8r_dot_protos_dot_common__pb2.Void.SerializeToString,
            ),
            'UpdateTunnelIds': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateTunnelIds,
                    request_deserializer=lte_dot_protos_dot_session__manager__pb2.UpdateTunnelIdsRequest.FromString,
                    response_serializer=lte_dot_protos_dot_session__manager__pb2.UpdateTunnelIdsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'magma.lte.LocalSessionManager', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class LocalSessionManager(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ReportRuleStats(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.LocalSessionManager/ReportRuleStats',
            lte_dot_protos_dot_session__manager__pb2.RuleRecordTable.SerializeToString,
            orc8r_dot_protos_dot_common__pb2.Void.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.LocalSessionManager/CreateSession',
            lte_dot_protos_dot_session__manager__pb2.LocalCreateSessionRequest.SerializeToString,
            lte_dot_protos_dot_session__manager__pb2.LocalCreateSessionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EndSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.LocalSessionManager/EndSession',
            lte_dot_protos_dot_session__manager__pb2.LocalEndSessionRequest.SerializeToString,
            lte_dot_protos_dot_session__manager__pb2.LocalEndSessionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BindPolicy2Bearer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.LocalSessionManager/BindPolicy2Bearer',
            lte_dot_protos_dot_session__manager__pb2.PolicyBearerBindingRequest.SerializeToString,
            lte_dot_protos_dot_session__manager__pb2.PolicyBearerBindingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetSessionRules(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.LocalSessionManager/SetSessionRules',
            lte_dot_protos_dot_session__manager__pb2.SessionRules.SerializeToString,
            orc8r_dot_protos_dot_common__pb2.Void.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateTunnelIds(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.LocalSessionManager/UpdateTunnelIds',
            lte_dot_protos_dot_session__manager__pb2.UpdateTunnelIdsRequest.SerializeToString,
            lte_dot_protos_dot_session__manager__pb2.UpdateTunnelIdsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class SessionProxyResponderStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ChargingReAuth = channel.unary_unary(
                '/magma.lte.SessionProxyResponder/ChargingReAuth',
                request_serializer=lte_dot_protos_dot_session__manager__pb2.ChargingReAuthRequest.SerializeToString,
                response_deserializer=lte_dot_protos_dot_session__manager__pb2.ChargingReAuthAnswer.FromString,
                )
        self.PolicyReAuth = channel.unary_unary(
                '/magma.lte.SessionProxyResponder/PolicyReAuth',
                request_serializer=lte_dot_protos_dot_session__manager__pb2.PolicyReAuthRequest.SerializeToString,
                response_deserializer=lte_dot_protos_dot_session__manager__pb2.PolicyReAuthAnswer.FromString,
                )


class SessionProxyResponderServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ChargingReAuth(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PolicyReAuth(self, request, context):
        """NOTE: if no session_id is specified, apply to all sessions for the IMSI
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SessionProxyResponderServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ChargingReAuth': grpc.unary_unary_rpc_method_handler(
                    servicer.ChargingReAuth,
                    request_deserializer=lte_dot_protos_dot_session__manager__pb2.ChargingReAuthRequest.FromString,
                    response_serializer=lte_dot_protos_dot_session__manager__pb2.ChargingReAuthAnswer.SerializeToString,
            ),
            'PolicyReAuth': grpc.unary_unary_rpc_method_handler(
                    servicer.PolicyReAuth,
                    request_deserializer=lte_dot_protos_dot_session__manager__pb2.PolicyReAuthRequest.FromString,
                    response_serializer=lte_dot_protos_dot_session__manager__pb2.PolicyReAuthAnswer.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'magma.lte.SessionProxyResponder', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SessionProxyResponder(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ChargingReAuth(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.SessionProxyResponder/ChargingReAuth',
            lte_dot_protos_dot_session__manager__pb2.ChargingReAuthRequest.SerializeToString,
            lte_dot_protos_dot_session__manager__pb2.ChargingReAuthAnswer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PolicyReAuth(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.SessionProxyResponder/PolicyReAuth',
            lte_dot_protos_dot_session__manager__pb2.PolicyReAuthRequest.SerializeToString,
            lte_dot_protos_dot_session__manager__pb2.PolicyReAuthAnswer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class CentralSessionControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateSession = channel.unary_unary(
                '/magma.lte.CentralSessionController/CreateSession',
                request_serializer=lte_dot_protos_dot_session__manager__pb2.CreateSessionRequest.SerializeToString,
                response_deserializer=lte_dot_protos_dot_session__manager__pb2.CreateSessionResponse.FromString,
                )
        self.UpdateSession = channel.unary_unary(
                '/magma.lte.CentralSessionController/UpdateSession',
                request_serializer=lte_dot_protos_dot_session__manager__pb2.UpdateSessionRequest.SerializeToString,
                response_deserializer=lte_dot_protos_dot_session__manager__pb2.UpdateSessionResponse.FromString,
                )
        self.TerminateSession = channel.unary_unary(
                '/magma.lte.CentralSessionController/TerminateSession',
                request_serializer=lte_dot_protos_dot_session__manager__pb2.SessionTerminateRequest.SerializeToString,
                response_deserializer=lte_dot_protos_dot_session__manager__pb2.SessionTerminateResponse.FromString,
                )


class CentralSessionControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateSession(self, request, context):
        """Notify OCS/PCRF of new session and return rules associated with subscriber
        along with credits for each rule
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateSession(self, request, context):
        """Updates OCS/PCRF with used credit and terminations from gateway
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TerminateSession(self, request, context):
        """Terminates session in OCS/PCRF for a subscriber
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CentralSessionControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateSession': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateSession,
                    request_deserializer=lte_dot_protos_dot_session__manager__pb2.CreateSessionRequest.FromString,
                    response_serializer=lte_dot_protos_dot_session__manager__pb2.CreateSessionResponse.SerializeToString,
            ),
            'UpdateSession': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateSession,
                    request_deserializer=lte_dot_protos_dot_session__manager__pb2.UpdateSessionRequest.FromString,
                    response_serializer=lte_dot_protos_dot_session__manager__pb2.UpdateSessionResponse.SerializeToString,
            ),
            'TerminateSession': grpc.unary_unary_rpc_method_handler(
                    servicer.TerminateSession,
                    request_deserializer=lte_dot_protos_dot_session__manager__pb2.SessionTerminateRequest.FromString,
                    response_serializer=lte_dot_protos_dot_session__manager__pb2.SessionTerminateResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'magma.lte.CentralSessionController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CentralSessionController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.CentralSessionController/CreateSession',
            lte_dot_protos_dot_session__manager__pb2.CreateSessionRequest.SerializeToString,
            lte_dot_protos_dot_session__manager__pb2.CreateSessionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.CentralSessionController/UpdateSession',
            lte_dot_protos_dot_session__manager__pb2.UpdateSessionRequest.SerializeToString,
            lte_dot_protos_dot_session__manager__pb2.UpdateSessionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TerminateSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.CentralSessionController/TerminateSession',
            lte_dot_protos_dot_session__manager__pb2.SessionTerminateRequest.SerializeToString,
            lte_dot_protos_dot_session__manager__pb2.SessionTerminateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class SetInterfaceForUserPlaneStub(object):
    """Set Interface from Pipelined
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetUPFNodeState = channel.unary_unary(
                '/magma.lte.SetInterfaceForUserPlane/SetUPFNodeState',
                request_serializer=lte_dot_protos_dot_session__manager__pb2.UPFNodeState.SerializeToString,
                response_deserializer=lte_dot_protos_dot_session__manager__pb2.SmContextVoid.FromString,
                )
        self.SetUPFSessionsConfig = channel.unary_unary(
                '/magma.lte.SetInterfaceForUserPlane/SetUPFSessionsConfig',
                request_serializer=lte_dot_protos_dot_session__manager__pb2.UPFSessionConfigState.SerializeToString,
                response_deserializer=lte_dot_protos_dot_session__manager__pb2.SmContextVoid.FromString,
                )
        self.SendPagingRequest = channel.unary_unary(
                '/magma.lte.SetInterfaceForUserPlane/SendPagingRequest',
                request_serializer=lte_dot_protos_dot_session__manager__pb2.UPFPagingInfo.SerializeToString,
                response_deserializer=lte_dot_protos_dot_session__manager__pb2.SmContextVoid.FromString,
                )


class SetInterfaceForUserPlaneServicer(object):
    """Set Interface from Pipelined
    """

    def SetUPFNodeState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetUPFSessionsConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendPagingRequest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SetInterfaceForUserPlaneServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SetUPFNodeState': grpc.unary_unary_rpc_method_handler(
                    servicer.SetUPFNodeState,
                    request_deserializer=lte_dot_protos_dot_session__manager__pb2.UPFNodeState.FromString,
                    response_serializer=lte_dot_protos_dot_session__manager__pb2.SmContextVoid.SerializeToString,
            ),
            'SetUPFSessionsConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.SetUPFSessionsConfig,
                    request_deserializer=lte_dot_protos_dot_session__manager__pb2.UPFSessionConfigState.FromString,
                    response_serializer=lte_dot_protos_dot_session__manager__pb2.SmContextVoid.SerializeToString,
            ),
            'SendPagingRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.SendPagingRequest,
                    request_deserializer=lte_dot_protos_dot_session__manager__pb2.UPFPagingInfo.FromString,
                    response_serializer=lte_dot_protos_dot_session__manager__pb2.SmContextVoid.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'magma.lte.SetInterfaceForUserPlane', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SetInterfaceForUserPlane(object):
    """Set Interface from Pipelined
    """

    @staticmethod
    def SetUPFNodeState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.SetInterfaceForUserPlane/SetUPFNodeState',
            lte_dot_protos_dot_session__manager__pb2.UPFNodeState.SerializeToString,
            lte_dot_protos_dot_session__manager__pb2.SmContextVoid.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetUPFSessionsConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.SetInterfaceForUserPlane/SetUPFSessionsConfig',
            lte_dot_protos_dot_session__manager__pb2.UPFSessionConfigState.SerializeToString,
            lte_dot_protos_dot_session__manager__pb2.SmContextVoid.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendPagingRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.SetInterfaceForUserPlane/SendPagingRequest',
            lte_dot_protos_dot_session__manager__pb2.UPFPagingInfo.SerializeToString,
            lte_dot_protos_dot_session__manager__pb2.SmContextVoid.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class AmfPduSessionSmContextStub(object):
    """SET API for 3 procedures request from AMF to SMF
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetAmfSessionContext = channel.unary_unary(
                '/magma.lte.AmfPduSessionSmContext/SetAmfSessionContext',
                request_serializer=lte_dot_protos_dot_session__manager__pb2.SetSMSessionContext.SerializeToString,
                response_deserializer=lte_dot_protos_dot_session__manager__pb2.SmContextVoid.FromString,
                )
        self.SetSmfNotification = channel.unary_unary(
                '/magma.lte.AmfPduSessionSmContext/SetSmfNotification',
                request_serializer=lte_dot_protos_dot_session__manager__pb2.SetSmNotificationContext.SerializeToString,
                response_deserializer=lte_dot_protos_dot_session__manager__pb2.SmContextVoid.FromString,
                )


class AmfPduSessionSmContextServicer(object):
    """SET API for 3 procedures request from AMF to SMF
    """

    def SetAmfSessionContext(self, request, context):
        """PDU session related configuration from amf to smf
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetSmfNotification(self, request, context):
        """PDU session related notification from amf to smf
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AmfPduSessionSmContextServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SetAmfSessionContext': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAmfSessionContext,
                    request_deserializer=lte_dot_protos_dot_session__manager__pb2.SetSMSessionContext.FromString,
                    response_serializer=lte_dot_protos_dot_session__manager__pb2.SmContextVoid.SerializeToString,
            ),
            'SetSmfNotification': grpc.unary_unary_rpc_method_handler(
                    servicer.SetSmfNotification,
                    request_deserializer=lte_dot_protos_dot_session__manager__pb2.SetSmNotificationContext.FromString,
                    response_serializer=lte_dot_protos_dot_session__manager__pb2.SmContextVoid.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'magma.lte.AmfPduSessionSmContext', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AmfPduSessionSmContext(object):
    """SET API for 3 procedures request from AMF to SMF
    """

    @staticmethod
    def SetAmfSessionContext(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.AmfPduSessionSmContext/SetAmfSessionContext',
            lte_dot_protos_dot_session__manager__pb2.SetSMSessionContext.SerializeToString,
            lte_dot_protos_dot_session__manager__pb2.SmContextVoid.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetSmfNotification(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.AmfPduSessionSmContext/SetSmfNotification',
            lte_dot_protos_dot_session__manager__pb2.SetSmNotificationContext.SerializeToString,
            lte_dot_protos_dot_session__manager__pb2.SmContextVoid.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class SmfPduSessionSmContextStub(object):
    """RPC service and method from SMF to AMF
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetAmfNotification = channel.unary_unary(
                '/magma.lte.SmfPduSessionSmContext/SetAmfNotification',
                request_serializer=lte_dot_protos_dot_session__manager__pb2.SetSmNotificationContext.SerializeToString,
                response_deserializer=lte_dot_protos_dot_session__manager__pb2.SmContextVoid.FromString,
                )
        self.SetSmfSessionContext = channel.unary_unary(
                '/magma.lte.SmfPduSessionSmContext/SetSmfSessionContext',
                request_serializer=lte_dot_protos_dot_session__manager__pb2.SetSMSessionContextAccess.SerializeToString,
                response_deserializer=lte_dot_protos_dot_session__manager__pb2.SmContextVoid.FromString,
                )


class SmfPduSessionSmContextServicer(object):
    """RPC service and method from SMF to AMF
    """

    def SetAmfNotification(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetSmfSessionContext(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SmfPduSessionSmContextServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SetAmfNotification': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAmfNotification,
                    request_deserializer=lte_dot_protos_dot_session__manager__pb2.SetSmNotificationContext.FromString,
                    response_serializer=lte_dot_protos_dot_session__manager__pb2.SmContextVoid.SerializeToString,
            ),
            'SetSmfSessionContext': grpc.unary_unary_rpc_method_handler(
                    servicer.SetSmfSessionContext,
                    request_deserializer=lte_dot_protos_dot_session__manager__pb2.SetSMSessionContextAccess.FromString,
                    response_serializer=lte_dot_protos_dot_session__manager__pb2.SmContextVoid.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'magma.lte.SmfPduSessionSmContext', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SmfPduSessionSmContext(object):
    """RPC service and method from SMF to AMF
    """

    @staticmethod
    def SetAmfNotification(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.SmfPduSessionSmContext/SetAmfNotification',
            lte_dot_protos_dot_session__manager__pb2.SetSmNotificationContext.SerializeToString,
            lte_dot_protos_dot_session__manager__pb2.SmContextVoid.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetSmfSessionContext(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/magma.lte.SmfPduSessionSmContext/SetSmfSessionContext',
            lte_dot_protos_dot_session__manager__pb2.SetSMSessionContextAccess.SerializeToString,
            lte_dot_protos_dot_session__manager__pb2.SmContextVoid.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
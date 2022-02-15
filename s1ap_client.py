# SPDX-FileCopyrightText: 2020 The Magma Authors.
# SPDX-FileCopyrightText: 2022 Open Networking Foundation <support@opennetworking.org>
#
# SPDX-License-Identifier: BSD-3-Clause

from typing import Dict, Optional

import grpc
from lte.protos.s1ap_service_pb2_grpc import S1apServiceStub
from common.service_registry import ServiceRegistry
from logger import EnodebdLogger as logger
from orc8r.protos.common_pb2 import Void

S1AP_SERVICE_NAME = "s1ap_service"
DEFAULT_GRPC_TIMEOUT = 20


def get_all_enb_state() -> Optional[Dict[int, int]]:
    """
    Make RPC call to 'GetENBState' method of s1ap service
    """
    try:
        chan = ServiceRegistry.get_rpc_channel(
            S1AP_SERVICE_NAME,
            ServiceRegistry.LOCAL,
        )
    except ValueError:
        logger.error('Cant get RPC channel to %s', S1AP_SERVICE_NAME)
        return {}
    client = S1apServiceStub(chan)
    try:
        res = client.GetENBState(Void(), DEFAULT_GRPC_TIMEOUT)
        return res.enb_state_map
    except grpc.RpcError as err:
        logger.warning(
            "GetEnbState error: [%s] %s",
            err.code(),
            err.details(),
        )
    return {}

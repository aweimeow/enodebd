# SPDX-FileCopyrightText: 2020 The Magma Authors.
# SPDX-FileCopyrightText: 2022 Open Networking Foundation <support@opennetworking.org>
#
# SPDX-License-Identifier: BSD-3-Clause

from threading import Thread
from typing import List
from unittest import mock

from lte.protos.mconfig import mconfigs_pb2
from configuration.service_configs import load_service_config
from common.sentry import sentry_init
from common.service import MagmaService
from enodeb_status import (
    get_operational_states,
    get_service_status_old,
)
from logger import EnodebdLogger as logger
from state_machines.enb_acs_manager import StateMachineManager
from orc8r.protos.service303_pb2 import State

from rpc_servicer import EnodebdRpcServicer
from stats_manager import StatsManager
from tr069.server import tr069_server
from prometheus_client import start_http_server as prometheus_start_http_server


def get_context(ip: str):
    with mock.patch('spyne.server.wsgi.WsgiApplication') as MockTransport:
        MockTransport.req_env = {"REMOTE_ADDR": ip}
        with mock.patch('spyne.server.wsgi.WsgiMethodContext') as MockContext:
            MockContext.transport = MockTransport
            return MockContext


def main():
    """
    Top-level function for enodebd
    """
    service = MagmaService('enodebd', mconfigs_pb2.EnodebD())
    logger.init()

    enodebd_cfg = load_service_config('enodebd')
    prometheus_cfg = enodebd_cfg.get("prometheus", None)

    if not prometheus_cfg:
        logger.warning("Prometheus configuration wasn't found in enodebd configuration.")
    else:
        prometheus_ip = prometheus_cfg.get("ip")
        prometheus_port = prometheus_cfg.get("port")
        prometheus_start_http_server(prometheus_port, addr=prometheus_ip)
        logger.info(
            "Starting Prometheus server on address %s:%d",
            prometheus_ip, prometheus_port)

    # Optionally pipe errors to Sentry
    sentry_init(service_name=service.name)

    # State machine manager for tracking multiple connected eNB devices.
    state_machine_manager = StateMachineManager(service)

    # Statistics manager
    stats_mgr = StatsManager(state_machine_manager)
    stats_mgr.run()

    # Start TR-069 thread
    server_thread = Thread(
        target=tr069_server,
        args=(state_machine_manager,),
        daemon=True,
    )
    server_thread.start()

    # Add all servicers to the server
    enodebd_servicer = EnodebdRpcServicer(state_machine_manager)
    enodebd_servicer.add_to_server(service.rpc_server)

    # Register function to get service status
    def get_enodebd_status():
        return get_service_status_old(state_machine_manager)
    service.register_get_status_callback(get_enodebd_status)

    # Register a callback function for GetOperationalStates service303 function
    def get_enodeb_operational_states() -> List[State]:
        return get_operational_states(state_machine_manager, service.mconfig)
    service.register_operational_states_callback(get_enodeb_operational_states)

    # Run the service loop
    service.run()

    # Cleanup the service
    service.close()


def call_repeatedly(loop, interval, function, *args, **kwargs):
    """
    Wrapper function to schedule function periodically
    """
    # Schedule next call
    loop.call_later(
        interval, call_repeatedly, loop, interval, function,
        *args, **kwargs,
    )
    # Call function
    function(*args, **kwargs)


if __name__ == "__main__":
    main()

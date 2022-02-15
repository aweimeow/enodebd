# SPDX-FileCopyrightText: 2020 The Magma Authors.
# SPDX-FileCopyrightText: 2022 Open Networking Foundation <support@opennetworking.org>
#
# SPDX-License-Identifier: BSD-3-Clause

import asyncio
from unittest import TestCase, main, mock

from common.service import MagmaService
from common.service_registry import ServiceRegistry
from orc8r.protos.common_pb2 import Void
from orc8r.protos.mconfig import mconfigs_pb2
from orc8r.protos.service303_pb2 import ServiceInfo
from orc8r.protos.service303_pb2_grpc import Service303Stub


class Service303Tests(TestCase):
    """
    Tests for the MagmaService and the Service303 interface
    """

    @mock.patch('time.time', mock.MagicMock(return_value=12345))
    def setUp(self):
        ServiceRegistry.add_service('test', '0.0.0.0', 0)
        self._stub = None

        self._loop = asyncio.new_event_loop()
        # Use a new event loop to ensure isolated tests
        self._service = MagmaService(
            name='test',
            empty_mconfig=mconfigs_pb2.MagmaD(),
            loop=self._loop,
        )
        asyncio.set_event_loop(self._service.loop)

    @mock.patch(
        'magma.common.service_registry.ServiceRegistry.get_proxy_config',
    )
    def test_service_run(self, mock_get_proxy_config):
        """
        Test if the service starts and stops gracefully.
        """

        self.assertEqual(self._service.state, ServiceInfo.STARTING)

        mock_get_proxy_config.return_value = {
            'cloud_address': '127.0.0.1',
            'proxy_cloud_connections': True,
        }

        # Start the service and pause the loop
        self._service.loop.stop()
        self._service.run()
        asyncio.set_event_loop(self._service.loop)
        self._service.log_counter._periodic_task.cancel()
        self.assertEqual(self._service.state, ServiceInfo.ALIVE)

        # Create a rpc stub and query the Service303 interface
        ServiceRegistry.add_service('test', '0.0.0.0', self._service.port)
        channel = ServiceRegistry.get_rpc_channel(
            'test',
            ServiceRegistry.LOCAL,
        )
        self._stub = Service303Stub(channel)

        info = ServiceInfo(
            name='test',
            version='0.0.0',
            state=ServiceInfo.ALIVE,
            health=ServiceInfo.APP_HEALTHY,
            start_time_secs=12345,
        )
        self.assertEqual(self._stub.GetServiceInfo(Void()), info)

        # Stop the service
        self._stub.StopService(Void())
        self._service.loop.run_forever()
        self.assertEqual(self._service.state, ServiceInfo.STOPPED)


if __name__ == "__main__":
    main()

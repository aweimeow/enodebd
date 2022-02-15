# SPDX-FileCopyrightText: 2020 The Magma Authors.
# SPDX-FileCopyrightText: 2022 Open Networking Foundation <support@opennetworking.org>
#
# SPDX-License-Identifier: BSD-3-Clause

from unittest import mock

from spyne.server.wsgi import WsgiMethodContext


def get_spyne_context_with_ip(
    req_ip: str = "192.168.60.145",
) -> WsgiMethodContext:
    with mock.patch('spyne.server.wsgi.WsgiApplication') as MockTransport:
        MockTransport.req_env = {"REMOTE_ADDR": req_ip}
        with mock.patch('spyne.server.wsgi.WsgiMethodContext') as MockContext:
            MockContext.transport = MockTransport
            return MockContext

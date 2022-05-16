# SPDX-FileCopyrightText: 2020 The Magma Authors.
# SPDX-FileCopyrightText: 2022 Open Networking Foundation <support@opennetworking.org>
#
# SPDX-License-Identifier: BSD-3-Clause

from typing import Any

GET_IP_FROM_IF_PATH = \
    'device_config.configuration_init.get_ip_from_if'

LOAD_SERVICE_MCONFIG_PATH = \
    'device_config.configuration_init.load_service_mconfig_as_json'


def mock_get_ip_from_if(
    _iface_name: str,
    _preference: Any = None,
) -> str:
    return '192.168.60.142'


def mock_load_service_mconfig_as_json(_service_name: str) -> Any:
    return {}

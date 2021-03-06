# SPDX-FileCopyrightText: 2020 The Magma Authors.
# SPDX-FileCopyrightText: 2022 Open Networking Foundation <support@opennetworking.org>
#
# SPDX-License-Identifier: BSD-3-Clause

from typing import Any as TAny
from typing import Dict

from google.protobuf.internal.well_known_types import Any
from configuration import service_configs
from configuration.exceptions import LoadConfigError


def filter_configs_by_key(configs_by_key: Dict[str, TAny]) -> Dict[str, TAny]:
    """
    Given a JSON-deserialized map of mconfig protobuf Any's keyed by service
    name, filter out any entires without a corresponding service or which have
    values that aren't registered in the protobuf symbol database yet.

    Args:
        configs_by_key:
            JSON-deserialized service mconfigs keyed by service name

    Returns:
        The input map without any services which currently don't exist.
    """
    magmad_cfg = service_configs.load_service_config('magmad')
    services = magmad_cfg.get('magma_services', [])
    services.append('magmad')
    services += magmad_cfg.get('registered_dynamic_services', [])
    services = set(services)

    filtered_configs_by_key = {}
    for srv, cfg in configs_by_key.items():
        if srv not in services:
            continue
        filtered_configs_by_key[srv] = cfg
    return filtered_configs_by_key


def unpack_mconfig_any(mconfig_any: Any, mconfig_struct: TAny) -> TAny:
    """
    Unpack a protobuf Any type into a given an empty protobuf message struct
    for a service.

    Args:
        mconfig_any: protobuf Any type to unpack
        mconfig_struct: protobuf message struct

    Returns: Concrete protobuf object that the provided Any wraps
    """
    unpacked = mconfig_any.Unpack(mconfig_struct)
    if not unpacked:
        raise LoadConfigError(
            'Cannot unpack Any type into message: %s' % mconfig_struct,
        )
    return mconfig_struct

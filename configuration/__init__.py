# SPDX-FileCopyrightText: 2020 The Magma Authors.
# SPDX-FileCopyrightText: 2022 Open Networking Foundation <support@opennetworking.org>
#
# SPDX-License-Identifier: BSD-3-Clause

import importlib
import logging

from configuration.exceptions import LoadConfigError
from configuration.service_configs import load_service_config

# Import all mconfig-providing modules so for the protobuf symbol database
try:
    mconfig_modules = load_service_config('magmad').get('mconfig_modules', [])
    for mod in mconfig_modules:
        logging.info('Importing mconfig module %s', mod)
        importlib.import_module(mod)
except LoadConfigError:
    logging.error('Could not load magmad yml config for mconfig modules')
    importlib.import_module('orc8r.protos.mconfig.mconfigs_pb2')

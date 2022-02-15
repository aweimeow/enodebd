# SPDX-FileCopyrightText: 2020 The Magma Authors.
# SPDX-FileCopyrightText: 2022 Open Networking Foundation <support@opennetworking.org>
#
# SPDX-License-Identifier: BSD-3-Clause

import os


def is_dev_mode() -> bool:
    """
    Returns whether the environment is set for dev mode
    """
    return os.environ.get('MAGMA_DEV_MODE') == '1'


def is_docker_network_mode() -> bool:
    """
    Returns whether the environment is set for dev mode
    """
    return os.environ.get('DOCKER_NETWORK_MODE') == '1'

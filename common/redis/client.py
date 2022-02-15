# SPDX-FileCopyrightText: 2020 The Magma Authors.
# SPDX-FileCopyrightText: 2022 Open Networking Foundation <support@opennetworking.org>
#
# SPDX-License-Identifier: BSD-3-Clause

import redis
from configuration.service_configs import get_service_config_value


def get_default_client():
    """
    Return a default redis client using the configured port in redis.yml
    """
    redis_port = get_service_config_value('redis', 'port', 6379)
    redis_addr = get_service_config_value('redis', 'bind', 'localhost')
    return redis.Redis(host=redis_addr, port=redis_port)

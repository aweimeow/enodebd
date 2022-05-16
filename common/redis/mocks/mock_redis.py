# SPDX-FileCopyrightText: 2020 The Magma Authors.
# SPDX-FileCopyrightText: 2022 Open Networking Foundation <support@opennetworking.org>
#
# SPDX-License-Identifier: BSD-3-Clause

from redis.exceptions import RedisError

# For non-failure cases, just use the fakeredis module


class MockUnavailableRedis(object):
    """
    MockUnavailableRedis implements a mock Redis Server that always raises
    a connection exception
    """

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def lock(self, key):
        raise RedisError("mock redis error")

    def keys(self, pattern=".*"):
        """ Mock keys with regex pattern matching."""
        raise RedisError("mock redis error")

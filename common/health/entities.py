# !/usr/bin/env python3

# SPDX-FileCopyrightText: 2020 The Magma Authors.
# SPDX-FileCopyrightText: 2022 Open Networking Foundation <support@opennetworking.org>
#
# SPDX-License-Identifier: BSD-3-Clause

import textwrap


class ActiveState:
    ACTIVE = 'active'
    RELOADING = 'reloading'
    INACTIVE = 'inactive'
    FAILED = 'failed'
    ACTIVATING = 'activating'
    DEACTIVATING = 'deactivating'

    dbus2state = {
        b'active': ACTIVE,
        b'reloading': RELOADING,
        b'inactive': INACTIVE,
        b'failed': FAILED,
        b'activating': ACTIVATING,
        b'deactivating': DEACTIVATING,
    }

    state2status = {
        ACTIVE: u'\u2714',
        RELOADING: u'\u27A4',
        INACTIVE: u'\u2717',
        FAILED: u'\u2717',
        ACTIVATING: u'\u27A4',
        DEACTIVATING: u'\u27A4',
    }


class Errors:
    def __init__(self, log_level, error_count):
        self.log_level = log_level
        self.error_count = error_count

    def __str__(self):
        return '{}: {}'.format(self.log_level, self.error_count)


class RestartFrequency:
    def __init__(self, count, time_interval):
        self.count = count
        self.time_interval = time_interval

    def __str__(self):
        return 'Restarted {} times {}'.format(
            self.count,
            self.time_interval,
        )


class HealthStatus:
    DOWN = 'Down'
    UP = 'Up'
    UNKNOWN = 'Unknown'


class Version:
    def __init__(self, version_code, last_update_time):
        self.version_code = version_code
        self.last_update_time = last_update_time

    def __str__(self):
        return '{}, last updated: {}'.format(
            self.version_code,
            self.last_update_time,
        )


class ServiceHealth:
    def __init__(
        self, service_name, active_state, sub_state,
        time_running, errors,
    ):
        self.service_name = service_name
        self.active_state = active_state
        self.sub_state = sub_state
        self.time_running = time_running
        self.errors = errors

    def __str__(self):
        return '{} {:20} {:10} {:15} {:10} {:>10} {:>10}'.format(
            ActiveState.state2status.get(self.active_state, '-'),
            self.service_name,
            self.active_state,
            self.sub_state,
            self.time_running,
            self.errors.log_level,
            self.errors.error_count,
        )


class HealthSummary:
    def __init__(
        self, version, platform,
        services_health,
        internet_health, dns_health,
        unexpected_restarts,
    ):
        self.version = version
        self.platform = platform
        self.services_health = services_health
        self.internet_health = internet_health
        self.dns_health = dns_health
        self.unexpected_restarts = unexpected_restarts

    def __str__(self):
        any_restarts = any([
            restarts.count
            for restarts in self.unexpected_restarts.values()
        ])
        return textwrap.dedent("""
            Running on {}
            Version: {}:
              {:20} {:10} {:15} {:10} {:>10} {:>10}
            {}

            Internet health: {}
            DNS health: {}

            Restart summary:
            {}
        """).format(
            self.version, self.platform,
            'Service', 'Status', 'SubState', 'Running for', 'Log level',
            'Errors since last restart',
            '\n'.join([str(h) for h in self.services_health]),
            self.internet_health, self.dns_health,
            '\n'.join([
                '{:20} {}'.format(name, restarts)
                for name, restarts
                in self.unexpected_restarts.items()
            ])
            if any_restarts
            else "No restarts since the gateway started",
        )

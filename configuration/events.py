# SPDX-FileCopyrightText: 2020 The Magma Authors.
# SPDX-FileCopyrightText: 2022 Open Networking Foundation <support@opennetworking.org>
#
# SPDX-License-Identifier: BSD-3-Clause

import snowflake
from eventd.eventd_client import log_event
from orc8r.protos.eventd_pb2 import Event


def deleted_stored_mconfig():
    log_event(
        Event(
            stream_name="magmad",
            event_type="deleted_stored_mconfig",
            tag=snowflake.snowflake(),
            value="{}",
        ),
    )


def updated_stored_mconfig():
    log_event(
        Event(
            stream_name="magmad",
            event_type="updated_stored_mconfig",
            tag=snowflake.snowflake(),
            value="{}",
        ),
    )

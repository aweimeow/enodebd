# SPDX-FileCopyrightText: 2020 The Magma Authors.
# SPDX-FileCopyrightText: 2022 Open Networking Foundation <support@opennetworking.org>
#
# SPDX-License-Identifier: BSD-3-Clause

from prometheus_client import Counter

STREAMER_RESPONSES = Counter(
    'streamer_responses',
    'The number of responses by label',
    ['result'],
)

SERVICE_ERRORS = Counter(
    'service_errors',
    'The number of errors logged',
)

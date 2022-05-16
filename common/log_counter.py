# SPDX-FileCopyrightText: 2020 The Magma Authors.
# SPDX-FileCopyrightText: 2022 Open Networking Foundation <support@opennetworking.org>
#
# SPDX-License-Identifier: BSD-3-Clause

import asyncio
from typing import Any

from common.job import Job
from common.log_count_handler import MsgCounterHandler
from common.metrics import SERVICE_ERRORS

# How frequently to poll systemd for error logs, in seconds
POLL_INTERVAL = 10


class ServiceLogErrorReporter(Job):
    """ Reports the number of logged errors for the service """

    def __init__(
        self,
        loop: asyncio.BaseEventLoop,
        service_config: Any,
        handler: MsgCounterHandler,
    ) -> None:
        super().__init__(interval=POLL_INTERVAL, loop=loop)
        self._service_config = service_config
        self._handler = handler

    async def _run(self):
        error_count = self._handler.pop_error_count()
        SERVICE_ERRORS.inc(error_count)

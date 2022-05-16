# SPDX-FileCopyrightText: 2020 The Magma Authors.
# SPDX-FileCopyrightText: 2022 Open Networking Foundation <support@opennetworking.org>
#
# SPDX-License-Identifier: BSD-3-Clause

from typing import Type

from devices.baicells import BaicellsHandler
from devices.baicells_old import BaicellsOldHandler
from devices.baicells_qafa import BaicellsQAFAHandler
from devices.baicells_qafb import BaicellsQAFBHandler
from devices.baicells_rts import BaicellsRTSHandler
from devices.device_utils import EnodebDeviceName
from devices.experimental.cavium import CaviumHandler
from devices.sercomm import SercommHandler
from state_machines.enb_acs import EnodebAcsStateMachine

# This exists only to break a circular dependency. Otherwise there's no
# point of having these names for the devices


DEVICE_HANDLER_BY_NAME = {
    EnodebDeviceName.BAICELLS: BaicellsHandler,
    EnodebDeviceName.BAICELLS_OLD: BaicellsOldHandler,
    EnodebDeviceName.BAICELLS_QAFA: BaicellsQAFAHandler,
    EnodebDeviceName.BAICELLS_QAFB: BaicellsQAFBHandler,
    EnodebDeviceName.BAICELLS_RTS: BaicellsRTSHandler,
    EnodebDeviceName.CAVIUM: CaviumHandler,
    EnodebDeviceName.SERCOMM: SercommHandler,
}


def get_device_handler_from_name(
    name: EnodebDeviceName,
) -> Type[EnodebAcsStateMachine]:
    return DEVICE_HANDLER_BY_NAME[name]

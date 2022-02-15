# SPDX-FileCopyrightText: 2020 The Magma Authors.
# SPDX-FileCopyrightText: 2022 Open Networking Foundation <support@opennetworking.org>
#
# SPDX-License-Identifier: BSD-3-Clause

from typing import NamedTuple, Optional

from lte.protos.mconfig.mconfigs_pb2 import EnodebD

EnodebConfig = NamedTuple(
    'EnodebConfig', [
        ('serial_num', str),
        ('config', EnodebD.EnodebConfig),
    ],
)


def get_enb_rf_tx_desired(mconfig: EnodebD, enb_serial: str) -> bool:
    """ True if the mconfig specifies to enable transmit on the eNB """
    if mconfig.enb_configs_by_serial is not None and \
            len(mconfig.enb_configs_by_serial) > 0:
        if enb_serial in mconfig.enb_configs_by_serial:
            enb_config = mconfig.enb_configs_by_serial[enb_serial]
            return enb_config.transmit_enabled
        else:
            raise KeyError('Missing eNB from mconfig: %s' % enb_serial)
    return mconfig.allow_enodeb_transmit


def is_enb_registered(mconfig: EnodebD, enb_serial: str) -> bool:
    """
    True if either:
        - the eNodeB is registered by serial to the Access Gateway
        or
        - the Access Gateway accepts all eNodeB devices
    """
    if mconfig.enb_configs_by_serial is not None and \
            len(mconfig.enb_configs_by_serial) > 0:
        if enb_serial in mconfig.enb_configs_by_serial:
            return True
        else:
            return False
    return True


def find_enb_by_cell_id(mconfig: EnodebD, cell_id: int) \
        -> Optional[EnodebConfig]:
    """
    Returns eNB config if:
        - the eNodeB is registered by serial to the Access Gateway
        - cell ID is found in eNB status by serial
    else: returns None
    """
    if mconfig.enb_configs_by_serial is not None and \
            len(mconfig.enb_configs_by_serial) > 0:
        for sn, enb in mconfig.enb_configs_by_serial.items():
            if cell_id == enb.cell_id:
                config = EnodebConfig(serial_num=sn, config=enb)
                return config
    return None

# SPDX-FileCopyrightText: 2020 The Magma Authors.
# SPDX-FileCopyrightText: 2022 Open Networking Foundation <support@opennetworking.org>
#
# SPDX-License-Identifier: BSD-3-Clause

# pylint: disable=protected-access
from unittest import TestCase

from lte.protos.enodebd_pb2 import SingleEnodebStatus
from devices.device_utils import EnodebDeviceName
from enodeb_status import (
    get_all_enb_status,
    get_enb_status,
    get_service_status_old,
    get_single_enb_status,
)
from state_machines.enb_acs_manager import StateMachineManager
from tests.test_utils.enb_acs_builder import (
    EnodebAcsStateMachineBuilder,
)
from tests.test_utils.spyne_builder import (
    get_spyne_context_with_ip,
)
from tests.test_utils.tr069_msg_builder import Tr069MessageBuilder


class EnodebStatusTests(TestCase):
    def test_get_service_status_old(self):
        manager = self._get_manager()
        status = get_service_status_old(manager)
        self.assertTrue(
            status['enodeb_connected'] == '0',
            'Should report no eNB connected',
        )

        ##### Start session for the first IP #####
        ctx1 = get_spyne_context_with_ip("192.168.60.145")
        # Send an Inform message, wait for an InformResponse
        inform_msg = Tr069MessageBuilder.get_inform(
            '48BF74',
            'BaiBS_RTS_3.1.6',
            '120200002618AGP0001',
        )
        manager.handle_tr069_message(ctx1, inform_msg)
        status = get_service_status_old(manager)
        self.assertTrue(
            status['enodeb_connected'] == '1',
            'Should report an eNB as conencted',
        )
        self.assertTrue(
            status['enodeb_serial'] == '120200002618AGP0001',
            'eNodeB serial should match the earlier Inform',
        )

    def test_get_enb_status(self):
        acs_state_machine = \
            EnodebAcsStateMachineBuilder\
            .build_acs_state_machine(EnodebDeviceName.BAICELLS)
        try:
            get_enb_status(acs_state_machine)
        except KeyError:
            self.fail(
                'Getting eNB status should succeed after constructor '
                'runs.',
            )

    def test_get_single_enb_status(self):
        manager = self._get_manager()
        ctx1 = get_spyne_context_with_ip("192.168.60.145")
        inform_msg = Tr069MessageBuilder.get_inform(
            '48BF74',
            'BaiBS_RTS_3.1.6',
            '120200002618AGP0001',
        )
        manager.handle_tr069_message(ctx1, inform_msg)
        status = get_single_enb_status('120200002618AGP0001', manager)
        self.assertEquals(
            status.connected,
            SingleEnodebStatus.StatusProperty.Value('ON'),
            'Status should be connected.',
        )
        self.assertEquals(
            status.configured,
            SingleEnodebStatus.StatusProperty.Value('OFF'),
            'Status should be not configured.',
        )

    def test_get_enodeb_all_status(self):
        manager = self._get_manager()

        ##### Test Empty #####
        enb_status_by_serial = get_all_enb_status(manager)
        self.assertTrue(enb_status_by_serial == {}, "No eNB connected")

        ##### Start session for the first IP #####
        ctx1 = get_spyne_context_with_ip("192.168.60.145")
        # Send an Inform message, wait for an InformResponse
        inform_msg = Tr069MessageBuilder.get_inform(
            '48BF74',
            'BaiBS_RTS_3.1.6',
            '120200002618AGP0001',
        )
        manager.handle_tr069_message(ctx1, inform_msg)
        enb_status_by_serial = get_all_enb_status(manager)
        enb_status = enb_status_by_serial.get('120200002618AGP0001')
        self.assertEquals(
            enb_status.enodeb_connected,
            SingleEnodebStatus.StatusProperty.Value('ON'),
            'Status should be connected.',
        )

    def _get_manager(self) -> StateMachineManager:
        service = EnodebAcsStateMachineBuilder.build_magma_service()
        return StateMachineManager(service)

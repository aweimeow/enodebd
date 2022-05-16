# SPDX-FileCopyrightText: 2020 The Magma Authors.
# SPDX-FileCopyrightText: 2022 Open Networking Foundation <support@opennetworking.org>
#
# SPDX-License-Identifier: BSD-3-Clause

import asyncio
from typing import Dict
from unittest import mock

from lte.protos.mconfig import mconfigs_pb2
from common.service import MagmaService
from devices.device_map import get_device_handler_from_name
from devices.device_utils import EnodebDeviceName
from state_machines.enb_acs import EnodebAcsStateMachine
from state_machines.enb_acs_manager import StateMachineManager
from tests.test_utils.config_builder import EnodebConfigBuilder


class EnodebAcsStateMachineBuilder:
    @classmethod
    def build_acs_manager(
        cls,
        device: EnodebDeviceName = EnodebDeviceName.BAICELLS,
    ) -> StateMachineManager:
        service = cls.build_magma_service(device)
        return StateMachineManager(service)

    @classmethod
    def build_multi_enb_acs_manager(
        cls,
    ) -> StateMachineManager:
        service = cls.build_multi_enb_magma_service()
        return StateMachineManager(service)

    @classmethod
    def build_multi_enb_acs_state_machine(
        cls,
        device: EnodebDeviceName = EnodebDeviceName.BAICELLS,
    ) -> EnodebAcsStateMachine:
        # Build the state_machine
        service = cls.build_multi_enb_magma_service()
        handler_class = get_device_handler_from_name(device)
        acs_state_machine = handler_class(service)
        return acs_state_machine

    @classmethod
    def build_acs_state_machine(
        cls,
        device: EnodebDeviceName = EnodebDeviceName.BAICELLS,
    ) -> EnodebAcsStateMachine:
        # Build the state_machine
        service = cls.build_magma_service(device)
        handler_class = get_device_handler_from_name(device)
        acs_state_machine = handler_class(service)
        return acs_state_machine

    @classmethod
    def build_magma_service(
        cls,
        device: EnodebDeviceName = EnodebDeviceName.BAICELLS,
            mconfig: mconfigs_pb2.EnodebD = None,
            service_config: Dict = None,
    ) -> MagmaService:
        event_loop = asyncio.get_event_loop()
        if not mconfig:
            mconfig = EnodebConfigBuilder.get_mconfig(device)
        if not service_config:
            service_config = EnodebConfigBuilder.get_service_config()
        with mock.patch('common.service.MagmaService') as MockService:
            MockService.config = service_config
            MockService.mconfig = mconfig
            MockService.loop = event_loop
            return MockService

    @classmethod
    def build_multi_enb_magma_service(cls) -> MagmaService:
        event_loop = asyncio.get_event_loop()
        mconfig = EnodebConfigBuilder.get_multi_enb_mconfig()
        service_config = EnodebConfigBuilder.get_service_config()
        with mock.patch('common.service.MagmaService') as MockService:
            MockService.config = service_config
            MockService.mconfig = mconfig
            MockService.loop = event_loop
            return MockService

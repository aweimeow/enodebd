# SPDX-FileCopyrightText: 2020 The Magma Authors.
# SPDX-FileCopyrightText: 2022 Open Networking Foundation <support@opennetworking.org>
#
# SPDX-License-Identifier: BSD-3-Clause

from state_machines.enb_acs import EnodebAcsStateMachine


class StateMachinePointer:
    """
    This is a hack to deal with the possibility that the specified data model
    doesn't match the eNB device enodebd ends up connecting to.

    When the data model doesn't match, the state machine is replaced with one
    that matches the data model.
    """

    def __init__(self, acs_state_machine: EnodebAcsStateMachine):
        self._acs_state_machine = acs_state_machine

    @property
    def state_machine(self):
        return self._acs_state_machine

    @state_machine.setter
    def state_machine(
        self,
        acs_state_machine: EnodebAcsStateMachine,
    ) -> None:
        self._acs_state_machine = acs_state_machine

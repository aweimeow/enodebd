# SPDX-FileCopyrightText: 2020 The Magma Authors.
# SPDX-FileCopyrightText: 2022 Open Networking Foundation <support@opennetworking.org>
#
# SPDX-License-Identifier: BSD-3-Clause

# pylint: disable=protected-access
from unittest import TestCase

from state_machines.timer import StateMachineTimer


class StateMachineTimerTests(TestCase):
    def test_is_done(self):
        timer_a = StateMachineTimer(0)
        self.assertTrue(timer_a.is_done(), 'Timer should be done')

        timer_b = StateMachineTimer(600)
        self.assertFalse(timer_b.is_done(), 'Timer should not be done')

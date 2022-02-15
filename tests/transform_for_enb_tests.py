# SPDX-FileCopyrightText: 2020 The Magma Authors.
# SPDX-FileCopyrightText: 2022 Open Networking Foundation <support@opennetworking.org>
#
# SPDX-License-Identifier: BSD-3-Clause

# pylint: disable=protected-access
from unittest import TestCase

from data_models.transform_for_enb import bandwidth


class TransformForMagmaTests(TestCase):
    def test_bandwidth(self) -> None:
        inp = 1.4
        out = bandwidth(inp)
        expected = 'n6'
        self.assertEqual(out, expected, 'Should work with a float')

        inp = 20
        out = bandwidth(inp)
        expected = 'n100'
        self.assertEqual(out, expected, 'Should work with an int')

        inp = 10
        out = bandwidth(inp)
        expected = 'n50'
        self.assertEqual(out, expected, 'Should work with int 10')

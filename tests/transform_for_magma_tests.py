# SPDX-FileCopyrightText: 2020 The Magma Authors.
# SPDX-FileCopyrightText: 2022 Open Networking Foundation <support@opennetworking.org>
#
# SPDX-License-Identifier: BSD-3-Clause

# pylint: disable=protected-access
from unittest import TestCase

from data_models.transform_for_magma import bandwidth, gps_tr181
from exceptions import ConfigurationError


class TransformForMagmaTests(TestCase):
    def test_gps_tr181(self) -> None:
        # Negative longitude
        inp = '-122150583'
        out = gps_tr181(inp)
        expected = '-122.150583'
        self.assertEqual(out, expected, 'Should convert negative longitude')

        inp = '122150583'
        out = gps_tr181(inp)
        expected = '122.150583'
        self.assertEqual(out, expected, 'Should convert positive longitude')

        inp = '0'
        out = gps_tr181(inp)
        expected = '0.0'
        self.assertEqual(out, expected, 'Should leave zero as zero')

    def test_bandwidth(self) -> None:
        inp = 'n6'
        out = bandwidth(inp)
        expected = 1.4
        self.assertEqual(out, expected, 'Should convert RBs')

        inp = 1.4
        out = bandwidth(inp)
        expected = 1.4
        self.assertEqual(out, expected, 'Should accept MHz')

        with self.assertRaises(ConfigurationError):
            inp = 'asdf'
            bandwidth(inp)

        with self.assertRaises(ConfigurationError):
            inp = 1234
            bandwidth(inp)

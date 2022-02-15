# SPDX-FileCopyrightText: 2020 The Magma Authors.
# SPDX-FileCopyrightText: 2022 Open Networking Foundation <support@opennetworking.org>
#
# SPDX-License-Identifier: BSD-3-Clause

# pylint: disable=protected-access

from unittest import TestCase

from devices.device_utils import (
    EnodebDeviceName,
    _parse_sw_version,
    get_device_name,
)
from exceptions import UnrecognizedEnodebError


class EnodebConfigUtilsTest(TestCase):
    def test_get_device_name(self) -> None:
        # Baicells
        oui = '34ED0B'
        version = 'BaiStation_V100R001C00B110SPC003'
        data_model = get_device_name(oui, version)
        expected = EnodebDeviceName.BAICELLS
        self.assertEqual(data_model, expected, 'Incorrect data model')

        # Baicells before bug-fix
        oui = '34ED0B'
        version = 'BaiStation_V100R001C00B110SPC002'
        data_model = get_device_name(oui, version)
        expected = EnodebDeviceName.BAICELLS_OLD
        self.assertEqual(data_model, expected, 'Incorrect data model')

        # Baicells QAFB
        oui = '48BF74'
        version = 'BaiBS_QAFB_some_version'
        data_model = get_device_name(oui, version)
        expected = EnodebDeviceName.BAICELLS_QAFB
        self.assertEqual(data_model, expected, 'Incorrect data model')

        # Cavium
        oui = '000FB7'
        version = 'Some version of Cavium'
        data_model = get_device_name(oui, version)
        expected = EnodebDeviceName.CAVIUM
        self.assertEqual(data_model, expected, 'Incorrect data model')

        # Unsupported device OUI
        oui = 'beepboopbeep'
        version = 'boopboopboop'
        with self.assertRaises(UnrecognizedEnodebError):
            get_device_name(oui, version)

        # Unsupported software version for Baicells
        oui = '34ED0B'
        version = 'blingblangblong'
        with self.assertRaises(UnrecognizedEnodebError):
            get_device_name(oui, version)

    def test_parse_version(self):
        """ Test that version string is parsed correctly """
        self.assertEqual(
            _parse_sw_version('BaiStation_V100R001C00B110SPC003'),
            [100, 1, 0, 110, 3],
        )
        self.assertEqual(
            _parse_sw_version('BaiStation_V100R001C00B060SPC012'),
            [100, 1, 0, 60, 12],
        )
        self.assertEqual(
            _parse_sw_version('BaiStation_V100R001C00B060SPC012_FB_3'),
            [100, 1, 0, 60, 12],
        )
        # Incorrect number of digits
        self.assertEqual(
            _parse_sw_version('BaiStation_V10R001C00B060SPC012'),
            None,
        )
        self.assertEqual(
            _parse_sw_version('XYZ123'),
            None,
        )
        self.assertEqual(
            _parse_sw_version(''),
            None,
        )

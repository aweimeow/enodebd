# SPDX-FileCopyrightText: 2020 The Magma Authors.
# SPDX-FileCopyrightText: 2022 Open Networking Foundation <support@opennetworking.org>
#
# SPDX-License-Identifier: BSD-3-Clause

# pylint: disable=protected-access

from unittest import TestCase

from data_models.data_model_parameters import ParameterName
from device_config.enodeb_configuration import EnodebConfiguration
from devices.experimental.cavium import CaviumTrDataModel


class EnodebConfigurationTest(TestCase):
    def setUp(self):
        self.config = EnodebConfiguration(CaviumTrDataModel)

    def tearDown(self):
        self.config = None

    def test_data_model(self) -> None:
        data_model = self.config.data_model
        expected = CaviumTrDataModel
        self.assertEqual(data_model, expected, 'Data model fetch incorrect')

    def test_get_has_set_parameter(self) -> None:
        param = ParameterName.ADMIN_STATE
        self.config.set_parameter(param, True)
        self.assertTrue(
            self.config.has_parameter(param),
            'Expected to have parameter',
        )
        param_value = self.config.get_parameter(param)
        expected = True
        self.assertEqual(
            param_value, expected,
            'Parameter value does not match what was set',
        )

    def test_add_has_delete_object(self) -> None:
        object_name = ParameterName.PLMN_N % 1
        self.assertFalse(self.config.has_object(object_name))
        self.config.add_object(object_name)
        self.assertTrue(self.config.has_object(object_name))
        self.config.delete_object(object_name)
        self.assertFalse(self.config.has_object(object_name))

    def test_get_parameter_names(self) -> None:
        # Should start off as an empty list
        names_list = self.config.get_parameter_names()
        self.assertEqual(len(names_list), 0, 'Expected 0 names')

        # Should grow as we set parameters
        self.config.set_parameter(ParameterName.ADMIN_STATE, True)
        names_list = self.config.get_parameter_names()
        self.assertEqual(len(names_list), 1, 'Expected 1 name')

        # Parameter names should not include objects
        self.config.add_object(ParameterName.PLMN)
        names_list = self.config.get_parameter_names()
        self.assertEqual(len(names_list), 1, 'Expected 1 name')

    def test_get_object_names(self) -> None:
        # Should start off as an empty list
        obj_list = self.config.get_object_names()
        self.assertEqual(len(obj_list), 0, 'Expected 0 names')

        # Should grow as we set parameters
        self.config.add_object(ParameterName.PLMN)
        obj_list = self.config.get_object_names()
        self.assertEqual(len(obj_list), 1, 'Expected 1 names')

    def test_get_set_parameter_for_object(self) -> None:
        self.config.add_object(ParameterName.PLMN_N % 1)
        self.config.set_parameter_for_object(
            ParameterName.PLMN_N_CELL_RESERVED % 1, True,
            ParameterName.PLMN_N % 1,
        )
        param_value = self.config.get_parameter_for_object(
            ParameterName.PLMN_N_CELL_RESERVED % 1, ParameterName.PLMN_N % 1,
        )
        self.assertTrue(
            param_value,
            'Expected that the param for object was set correctly',
        )

    def test_get_parameter_names_for_object(self) -> None:
        # Should start off empty
        self.config.add_object(ParameterName.PLMN_N % 1)
        param_list = self.config.get_parameter_names_for_object(
            ParameterName.PLMN_N % 1,
        )
        self.assertEqual(len(param_list), 0, 'Should be an empty param list')

        # Should increment as we set parameters
        self.config.set_parameter_for_object(
            ParameterName.PLMN_N_CELL_RESERVED % 1, True,
            ParameterName.PLMN_N % 1,
        )
        param_list = self.config.get_parameter_names_for_object(
            ParameterName.PLMN_N % 1,
        )
        self.assertEqual(len(param_list), 1, 'Should not be an empty list')

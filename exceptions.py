# SPDX-FileCopyrightText: 2020 The Magma Authors.
# SPDX-FileCopyrightText: 2022 Open Networking Foundation <support@opennetworking.org>
#
# SPDX-License-Identifier: BSD-3-Clause


class ConfigurationError(Exception):
    """ Indicates that the eNodeB could not be configured correctly. """
    pass


class Tr069Error(Exception):
    pass


class IncorrectDeviceHandlerError(Exception):
    """ Indicates that we're using the wrong data model for configuration. """

    def __init__(self, device_name: str):
        """
        device_name: What device we actually are dealing with
        """
        super().__init__()
        self.device_name = device_name


class UnrecognizedEnodebError(Exception):
    """
    Indicates that the Access Gateway does not recognize the eNodeB.
    The Access Gateway will not interact with the eNodeB in question.
    """
    pass

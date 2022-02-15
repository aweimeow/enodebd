# SPDX-FileCopyrightText: 2020 The Magma Authors.
# SPDX-FileCopyrightText: 2022 Open Networking Foundation <support@opennetworking.org>
#
# SPDX-License-Identifier: BSD-3-Clause

from abc import ABC, abstractmethod
from typing import Any

from device_config.enodeb_configuration import EnodebConfiguration


class EnodebConfigurationPostProcessor(ABC):
    """
    Overrides the desired configuration for the eNodeB, with subclass per
    device/sw-version that requires non-standard configuration behavior.
    """

    @abstractmethod
    def postprocess(self, mconfig: Any, service_cfg: Any, desired_cfg: EnodebConfiguration) -> None:
        """
        Implementation of function which overrides the desired configuration
        for the eNodeB
        """
        pass

"""
Copyright 2020 The Magma Authors.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from typing import Type

from devices.baicells import BaicellsHandler
from devices.baicells_old import BaicellsOldHandler
from devices.baicells_qafa import BaicellsQAFAHandler
from devices.baicells_qafb import BaicellsQAFBHandler
from devices.baicells_rts import BaicellsRTSHandler
from devices.device_utils import EnodebDeviceName
from devices.experimental.cavium import CaviumHandler
from devices.freedomfi_one import FreedomFiOneHandler
from state_machines.enb_acs import EnodebAcsStateMachine

# This exists only to break a circular dependency. Otherwise there's no
# point of having these names for the devices


DEVICE_HANDLER_BY_NAME = {
    EnodebDeviceName.BAICELLS: BaicellsHandler,
    EnodebDeviceName.BAICELLS_OLD: BaicellsOldHandler,
    EnodebDeviceName.BAICELLS_QAFA: BaicellsQAFAHandler,
    EnodebDeviceName.BAICELLS_QAFB: BaicellsQAFBHandler,
    EnodebDeviceName.BAICELLS_RTS: BaicellsRTSHandler,
    EnodebDeviceName.CAVIUM: CaviumHandler,
    EnodebDeviceName.FREEDOMFI_ONE: FreedomFiOneHandler,
}


def get_device_handler_from_name(
    name: EnodebDeviceName,
) -> Type[EnodebAcsStateMachine]:
    return DEVICE_HANDLER_BY_NAME[name]
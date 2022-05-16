# SPDX-FileCopyrightText: 2020 The Magma Authors.
# SPDX-FileCopyrightText: 2022 Open Networking Foundation <support@opennetworking.org>
#
# SPDX-License-Identifier: BSD-3-Clause

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

from prometheus_client import Counter, Gauge

# Gauges for current eNodeB status
STAT_ENODEB_CONNECTED = Gauge(
    'enodeb_mgmt_connected',
    'ENodeB management plane connected',
)
STAT_ENODEB_CONFIGURED = Gauge(
    'enodeb_mgmt_configured',
    'ENodeB is in configured state',
)
STAT_OPSTATE_ENABLED = Gauge(
    'enodeb_opstate_enabled',
    'ENodeB operationally enabled',
)
STAT_RF_TX_ENABLED = Gauge(
    'enodeb_rf_tx_enabled',
    'ENodeB RF transmitter enabled',
)
STAT_RF_TX_DESIRED = Gauge(
    'enodeb_rf_tx_desired',
    'ENodeB RF transmitter desired state',
)
STAT_GPS_CONNECTED = Gauge(
    'enodeb_gps_connected',
    'ENodeB GPS synchronized',
)
STAT_PTP_CONNECTED = Gauge(
    'enodeb_ptp_connected',
    'ENodeB PTP/1588 synchronized',
)
STAT_MME_CONNECTED = Gauge(
    'enodeb_mme_connected',
    'ENodeB connected to MME',
)
STAT_ENODEB_REBOOT_TIMER_ACTIVE = Gauge(
    'enodeb_reboot_timer_active',
    'Timer for ENodeB reboot active',
)
STAT_ENODEB_REBOOTS = Counter(
    'enodeb_reboots',
    'ENodeB reboots by enodebd', ['cause'],
)

# Metrics that are accumulated by eNodeB. Use gauges to avoid 'double-counting',
# since eNodeB does accumulation.
STAT_RRC_ESTAB_ATT = Gauge(
    'rrc_estab_attempts', 'RRC establishment attempts',
)
STAT_RRC_ESTAB_SUCC = Gauge(
    'rrc_estab_successes', 'RRC establishment successes',
)
STAT_RRC_REESTAB_ATT = Gauge(
    'rrc_reestab_attempts', 'RRC re-establishment attempts',
)
STAT_RRC_REESTAB_ATT_RECONF_FAIL = Gauge(
    'rrc_reestab_attempts_reconf_fail',
    'RRC re-establishment attempts due to reconfiguration failure',
)
STAT_RRC_REESTAB_ATT_HO_FAIL = Gauge(
    'rrc_reestab_attempts_ho_fail',
    'RRC re-establishment attempts due to handover failure',
)
STAT_RRC_REESTAB_ATT_OTHER = Gauge(
    'rrc_reestab_attempts_other',
    'RRC re-establishment attempts due to other cause',
)
STAT_RRC_REESTAB_SUCC = Gauge(
    'rrc_reestab_successes', 'RRC re-establishment successes',
)
STAT_ERAB_ESTAB_ATT = Gauge(
    'erab_estab_attempts', 'ERAB establishment attempts',
)
STAT_ERAB_ESTAB_SUCC = Gauge(
    'erab_estab_successes', 'ERAB establishment successes',
)
STAT_ERAB_ESTAB_FAIL = Gauge(
    'erab_estab_failures', 'ERAB establishment failures',
)
STAT_ERAB_REL_REQ = Gauge(
    'erab_release_requests', 'ERAB release requests',
)
STAT_ERAB_REL_REQ_USER_INAC = Gauge(
    'erab_release_requests_user_inactivity',
    'ERAB release requests due to user inactivity',
)
STAT_ERAB_REL_REQ_NORMAL = Gauge(
    'erab_release_requests_normal', 'ERAB release requests due to normal cause',
)
STAT_ERAB_REL_REQ_RES_NOT_AVAIL = Gauge(
    'erab_release_requests_radio_resources_not_available',
    'ERAB release requests due to radio resources not available',
)
STAT_ERAB_REL_REQ_REDUCE_LOAD = Gauge(
    'erab_release_requests_reduce_load',
    'ERAB release requests due to reducing load in serving cell',
)
STAT_ERAB_REL_REQ_FAIL_IN_RADIO = Gauge(
    'erab_release_requests_fail_in_radio_proc',
    'ERAB release requests due to failure in the radio interface procedure',
)
STAT_ERAB_REL_REQ_EUTRAN_REAS = Gauge(
    'erab_release_requests_eutran_reas',
    'ERAB release requests due to EUTRAN generated reasons',
)
STAT_ERAB_REL_REQ_RADIO_CONN_LOST = Gauge(
    'erab_release_requests_radio_radio_conn_lost',
    'ERAB release requests due to radio connection with UE lost',
)
STAT_ERAB_REL_REQ_OAM_INTV = Gauge(
    'erab_release_requests_oam_intervention',
    'ERAB release requests due to OAM intervention',
)
STAT_PDCP_USER_PLANE_BYTES_UL = Gauge(
    'pdcp_user_plane_bytes_ul', 'User plane uplink bytes at PDCP', ['enodeb'],
)
STAT_PDCP_USER_PLANE_BYTES_DL = Gauge(
    'pdcp_user_plane_bytes_dl', 'User plane downlink bytes at PDCP', ['enodeb'],
)

# Aether-use Status

STAT_ENODEB_LAST_CONFIGURED_TIME = Gauge(
    'enodeb_last_configured_time',
    'Information of configured eNodeB', ['serial_number', 'ip_address']
)

STATE_ENODEB_CURRENT_STATUS = Gauge(
    'enodeb_current_status', 'The Current Configuration Status of specific enodeb', [
        'serial_number',
        'connected', 'disconnected', 'firmware_upgrading', 'configured'
    ]
)

STATE_ENODEB_GPS_STATUS = Gauge(
    'enodeb_gps_status', 'The Current GPS Status of specific enodeb', [
        'serial_number'
    ]
)

STATE_ENODEB_GPS_STATUS_LAT = Gauge(
    'enodeb_gps_status_lat', 'The Current GPS Latitude Status of specific enodeb', [
        'serial_number'
    ]
)

STATE_ENODEB_GPS_STATUS_LONG = Gauge(
    'enodeb_gps_status_long', 'The Current GPS Longtitude Status of specific enodeb', [
        'serial_number'
    ]
)

STATE_ENODEB_OP_STATE = Gauge(
    'enodeb_op_status', 'The Current Operating Status of specific enodeb', [
        'serial_number', 'op_state'
    ]
)

# key = serial number / value = labels (serial_number, ip_address, )
stat_enodeb_last_configured_time_dict = dict()
# key = serial number / value = labels (sn, connected, disconnected, firmware_upgrading, configured)
state_enodeb_current_status_dict = dict()
state_enodeb_op_status_dict = dict()


def set_enb_last_configured_time(serial_number, ip_address, time):
    if serial_number in stat_enodeb_last_configured_time_dict:
        STAT_ENODEB_LAST_CONFIGURED_TIME.remove(
            *stat_enodeb_last_configured_time_dict.pop(serial_number)
        )
    else:
        stat_enodeb_last_configured_time_dict[serial_number] = [
            serial_number, ip_address
        ]

    STAT_ENODEB_LAST_CONFIGURED_TIME.labels(
        serial_number=serial_number,
        ip_address=ip_address
    ).set(time)

def set_enb_status(serial_number, status=["connected", "disconnected", "firmware_upgrading", "configured"]):
    status_list = ["connected", "disconnected", "firmware_upgrading", "configured"]

    if serial_number in state_enodeb_current_status_dict:
        STATE_ENODEB_CURRENT_STATUS.remove(
            *state_enodeb_current_status_dict.pop(serial_number)
        )
    else:
        state_enodeb_current_status_dict[serial_number] = [
            serial_number,
            int(status == "connected"),
            int(status == "disconnected"),
            int(status == "firmware_upgrading"),
            int(status == "configured")
        ]

    STATE_ENODEB_CURRENT_STATUS.labels(
        serial_number=serial_number,
        connected=int(status == "connected"),
        disconnected=int(status == "disconnected"),
        firmware_upgrading=int(status == "firmware_upgrading"),
        configured=int(status == "configured")
    ).set(status_list.index(status))

def set_enb_gps_status(serial_number, lat, long, gps_state):
    mapped_status = int()
    if gps_state in ["Success", "Running", "1"]:
        mapped_status = 1
    else:
        mapped_status = 0

    lat_div_million = float(lat) / 1000000
    lon_div_million = float(long) / 1000000

    STATE_ENODEB_GPS_STATUS.labels(serial_number=serial_number).set(mapped_status)
    STATE_ENODEB_GPS_STATUS_LAT.labels(serial_number=serial_number).set(lat_div_million)
    STATE_ENODEB_GPS_STATUS_LONG.labels(serial_number=serial_number).set(lon_div_million)

def set_enb_op_status(serial_number, op_state):
    mapped_status = int()
    if op_state in ["enabled"]:
        mapped_status = 1
    else:
        mapped_status = 0

    if serial_number in state_enodeb_op_status_dict:
        STATE_ENODEB_OP_STATE.remove(
            *state_enodeb_op_status_dict.pop(serial_number)
        )
    else:
        state_enodeb_op_status_dict[serial_number] = [
            serial_number, op_state
        ]

    STATE_ENODEB_OP_STATE.labels(
        serial_number=serial_number, op_state=op_state
    ).set(mapped_status)
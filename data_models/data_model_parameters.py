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


class ParameterName():
    # Top-level objects
    DEVICE = 'Device'
    FAP_SERVICE = 'FAPService'

    # Device info parameters
    GPS_STATUS = 'GPS status'
    PTP_STATUS = 'PTP status'
    MME_STATUS = 'MME status'
    REM_STATUS = 'REM status'

    LOCAL_GATEWAY_ENABLE = 'Local gateway enable'
    GPS_ENABLE = 'GPS enable'
    GPS_LAT = 'GPS lat'
    GPS_LONG = 'GPS long'
    SW_VERSION = 'SW version'

    SERIAL_NUMBER = 'Serial number'
    CELL_ID = 'Cell ID'
    IP_ADDRESS = "ip_address"

    # Capabilities
    DUPLEX_MODE_CAPABILITY = 'Duplex mode capability'
    BAND_CAPABILITY = 'Band capability'

    # RF-related parameters
    EARFCNDL = 'earfcndl1'
    EARFCNUL = 'earfcnul1'
    EARFCNDL2 = 'earfcndl2'
    EARFCNUL2 = 'earfcnul2'
    EARFCNDL_LIST = 'earfcndl_list'
    EARFCNUL_LIST = 'earfcnul_list'

    FREQ_BAND_1 = "freq_band_1"
    FREQ_BAND_2 = "freq_band_2"
    FREQ_BAND_LIST = "freq_band_list"

    BAND = 'Band'
    PCI = 'PCI'
    DL_BANDWIDTH = 'DL bandwidth'
    UL_BANDWIDTH = 'UL bandwidth'
    SUBFRAME_ASSIGNMENT = 'Subframe assignment'
    SPECIAL_SUBFRAME_PATTERN = 'Special subframe pattern'
    TX_POWER = "tx_power"
    TUNNEL_TYPE = "tunnel_type"

    # Radio Resource Management (RRM) parameters
    CARRIER_AGG_ENABLE = "carrier_agg_enable"
    CARRIER_NUMBER = "carrier_number"
    CONTIGUOUS_CC = "contiguous_cc"

    # Other LTE parameters
    ADMIN_STATE = 'Admin state'
    OP_STATE = 'Opstate'
    RF_TX_STATUS = 'RF TX status'

    # RAN parameters
    CELL_RESERVED = 'Cell reserved'
    CELL_BARRED = 'Cell barred'
    PRIM_SOURCE = "prim_source"

    # Core network parameters
    MME_IP = 'MME IP'
    MME_PORT = 'MME port'
    NUM_PLMNS = 'Num PLMNs'
    PLMN = 'PLMN'
    PLMN_LIST = 'PLMN List'

    # PLMN parameters
    PLMN_N = 'PLMN %d'
    PLMN_N_CELL_RESERVED = 'PLMN %d cell reserved'
    PLMN_N_ENABLE = 'PLMN %d enable'
    PLMN_N_PRIMARY = 'PLMN %d primary'
    PLMN_N_PLMNID = 'PLMN %d PLMNID'

    # PLMN arrays are added below
    TAC = 'tac'
    TAC2 = 'tac2'
    IP_SEC_ENABLE = 'IPSec enable'
    MME_POOL_ENABLE = 'MME pool enable'

    # Management server parameters
    PERIODIC_INFORM_ENABLE = 'Periodic inform enable'
    PERIODIC_INFORM_INTERVAL = 'Periodic inform interval'
    ENABLE_CWMP = "enable_cwmp"

    # Performance management parameters
    PERF_MGMT_ENABLE = 'Perf mgmt enable'
    PERF_MGMT_UPLOAD_INTERVAL = 'Perf mgmt upload interval'
    PERF_MGMT_UPLOAD_URL = 'Perf mgmt upload URL'
    PERF_MGMT_USER = 'Perf mgmt username'
    PERF_MGMT_PASSWORD = 'Perf mgmt password'

    SAS_ENABLE = "sas_enabled"
    SAS_SERVER_URL = "sas_server_url"
    SAS_UID = "sas_uid"
    SAS_CATEGORY = "sas_category"
    SAS_CHANNEL_TYPE = "sas_channel_type"
    SAS_CERT_SUBJECT = "sas_cert_subject"
    SAS_IC_GROUP_ID = "sas_icg_group_id"
    SAS_LOCATION = "sas_location"
    SAS_HEIGHT_TYPE = "sas_height_type"
    SAS_FCCID = "sas_fccid"
    SAS_MEAS_CAPS = "sas_measure_capability"
    SAS_MANU_ENABLE = "sas_manufacturer_prefix_enable"

    SAS_CPI_ENABLE = "sas_cpi_enable"
    SAS_CPI_IPE = "sas_cpi_ipe"
    SAS_CPI_NAME = "sas_cpi_name"
    SAS_CPI_ID = "sas_cpi_id"
    SAS_CPI_DATA = "sas_cpi_signature_data"
    SAS_ANTA_AZIMUTH = "sas_antenna_azimuth"
    SAS_ANTA_DOWNTILT = "sas_antenna_downtilt"
    SAS_ANTA_GAIN = "sas_antenna_gain"
    SAS_ANTA_BEAMWIDTH = "sas_antenna_beamwidth"


class TrParameterType():
    BOOLEAN = 'boolean'
    STRING = 'string'
    INT = 'int'
    UNSIGNED_INT = 'unsignedInt'
    OBJECT = 'object'

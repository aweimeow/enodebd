# SPDX-FileCopyrightText: 2020 The Magma Authors.
# SPDX-FileCopyrightText: 2022 Open Networking Foundation <support@opennetworking.org>
#
# SPDX-License-Identifier: BSD-3-Clause

class ParameterName():
    # Top-level objects
    DEVICE = 'Device'
    FAP_SERVICE = 'FAPService'

    # Device info parameters
    GPS_STATUS = 'gps_status'
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
    EARFCNDL = 'earfcn_downlink1'
    EARFCNUL = 'earfcn_uplink1'
    EARFCNDL2 = 'earfcn_downlink2'
    EARFCNUL2 = 'earfcn_uplink2'
    EARFCNDL_LIST = 'earfcn_downlink_list'
    EARFCNUL_LIST = 'earfcn_uplink_list'

    FREQ_BAND_1 = "frequency_band_1"
    FREQ_BAND_2 = "frequency_band_2"
    FREQ_BAND_LIST = "freq_band_list"

    BAND = 'Band'
    PCI = 'PCI'
    DL_BANDWIDTH = 'downlink_bandwidth'
    UL_BANDWIDTH = 'uplink_bandwidth'
    TX_POWER = "tx_power"
    TUNNEL_TYPE = "tunnel_type"

    # Radio Resource Management (RRM) parameters
    CARRIER_AGG_ENABLE = "carrier_agg_enable"
    CARRIER_NUMBER = "carrier_number"
    CONTIGUOUS_CC = "is_ca_frequency_contiguous"

    # Other LTE parameters
    ADMIN_STATE = 'admin_state'
    OP_STATE = 'Opstate'
    RF_TX_STATUS = 'RF TX status'

    # RAN parameters
    CELL_RESERVED = 'Cell reserved'
    CELL_BARRED = 'Cell barred'
    PRIM_SOURCE = "primary_source"

    # Cell parameters
    CELL_ENABLE64QAM = "enable64qam"
    SPECIAL_SUBFRAME_PATTERN = 'subframe_configuration'
    SUBFRAME_ASSIGNMENT = 'subframe_assignment'

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
    IP_SEC_ENABLE = 'ipsec_enable'
    MME_POOL_ENABLE = 'mme_pool_enable'

    # Management server parameters
    PERIODIC_INFORM_ENABLE = 'periodic_inform_enable'
    PERIODIC_INFORM_INTERVAL = 'periodic_inform_interval'
    CWMP_ENABLE = "cwmp_enable"

    # Performance management parameters
    PERF_MGMT_ENABLE = 'perf_mgmt_enable'
    PERF_MGMT_UPLOAD_INTERVAL = 'perf_mgmt_upload_interval'
    PERF_MGMT_UPLOAD_URL = 'perf_mgmt_upload_url'
    PERF_MGMT_USER = 'perf_mgmt_username'
    PERF_MGMT_PASSWORD = 'perf_mgmt_password'

    SAS_ENABLE = "sas_enable"
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
    SAS_MANU_ENABLE = "manufacturer_prefix_enable"

    SAS_CPI_ENABLE = "cpi_enable"
    SAS_CPI_IPE = "sas_cpi_ipe"
    SAS_CPI_NAME = "sas_cpi_name"
    SAS_CPI_ID = "sas_cpi_id"
    SAS_CPI_DATA = "sas_cpi_signature_data"
    SAS_ANTA_AZIMUTH = "sas_antenna_azimuth"
    SAS_ANTA_DOWNTILT = "sas_antenna_downtilt"
    SAS_ANTA_GAIN = "sas_antenna_gain"
    SAS_ANTA_BEAMWIDTH = "sas_antenna_beamwidth"

    FIRMWARE_VERSION = "firmware_version"
    FIRMWARE_URL = "firmware_url"
    FIRMWARE_SIZE = "firmware_size"


class TrParameterType():
    BOOLEAN = 'boolean'
    STRING = 'string'
    INT = 'int'
    UNSIGNED_INT = 'unsignedInt'
    OBJECT = 'object'

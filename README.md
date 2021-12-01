# ENODEBD

eNodeB daemon is an Automatic Configuration Server (ACS) which forks from [Facebook Magma project](https://github.com/magma/magma). It currently tested with Sercomm eNodeB P27-SCE4255W small cell.

# Configuration

We have these configuration files for configuring eNodeBD service.

1. override_configs/gateway.mconfig

The enodebd will generate the empty configuration to config service, and it will load
`override_configs/gateway.mconfig` to fill in the empty configuration.

2. magma_configs/acs_common.yml

The `acs_common.yml` will hold the default value for all eNodeBs, like as the PLMN may be a shared value among all eNodeBs.

3. magma_configs/serial_numbers/_2009CW5000019_.yml

The `serial_number.yml` will have the customized value for each configurable parameters. The value in `serial_number.yml` will override the value defines in `gateway.mconfig` and `acs_common.yml` when corresponding eNodeB connects (base on the serial number provided by eNodeB).
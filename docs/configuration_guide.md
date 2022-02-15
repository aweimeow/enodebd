# eNodeBD Configuration Guide

eNodeBD (eNodeB daemon), which also called ACS(Automatic Configuration Server), is using for configuring and operating eNodeB by programmed steps.

In the beginning, we need to learn what configuration eNodeBD have, and how to configure it as we need.

## magma_configs/serial_number/`{serial_number}`.yml

This file needs to be named exactly same as the enodeb's serial number, when a new eNodeB register to ACS, ACS will ask eNodeB to provide serial number and other information for giving a proper configuration to eNodeB, and ACS will search in this directory to find if there has a configuration for specific eNodeB. If no configuration file found, it will use Magma default configuration for eNodeB.

## magma_configs/acs_common.yml

This file provides the common parameter for generating eNodeB-specific configuration, if the `{serial_number}.yml` doesn't provide with the value of parameters, ACS will use the value declared in `acs_common.yml` in generated configuration.

## override_configs/gateway.mconfig

The configuration of eNodeBD services, included default configuration for unknown eNodeB, and also the log level of eNodeBD.
# SPDX-FileCopyrightText: 2020 The Magma Authors.
# SPDX-FileCopyrightText: 2022 Open Networking Foundation <support@opennetworking.org>
#
# SPDX-License-Identifier: BSD-3-Clause

from common.sentry import sentry_init
from common.service import MagmaService
from eventd.event_validator import EventValidator
from eventd.rpc_servicer import EventDRpcServicer
from orc8r.protos.mconfig.mconfigs_pb2 import EventD


def main():
    """ main() for eventd """
    service = MagmaService('eventd', EventD())

    # Optionally pipe errors to Sentry
    sentry_init(service_name=service.name)

    event_validator = EventValidator(service.config)
    eventd_servicer = EventDRpcServicer(service.config, event_validator)
    eventd_servicer.add_to_server(service.rpc_server)

    # Run the service loop
    service.run()

    # Cleanup the service
    service.close()


if __name__ == "__main__":
    main()

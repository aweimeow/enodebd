# SPDX-FileCopyrightText: 2020 The Magma Authors.
# SPDX-FileCopyrightText: 2022 Open Networking Foundation <support@opennetworking.org>
#
# SPDX-License-Identifier: BSD-3-Clause

import os
import sys

from grpc.tools import protoc


def gen_prometheus_proto_py(proto_file_dir, output_dir):
    # Function For fb-internal build tools - open source should use this file
    # as a script
    protoc.main(
        (
            '',
            '-I' + proto_file_dir,
            '--python_out=' + output_dir,
            '--grpc_python_out=' + output_dir,
            os.path.join(proto_file_dir, 'metrics.proto'),
        ),
    )


if __name__ == '__main__':
    # ./gen_prometheus_proto.py <magma root> <output_dir>
    magma_root, out_dir = sys.argv[1], sys.argv[2]
    file_dir = os.path.join(magma_root, 'proto_files/orc8r/protos/prometheus')
    gen_prometheus_proto_py(file_dir, out_dir)


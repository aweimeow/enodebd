# Magma enodebd

## Generate protos

```bash
python tools/gen_protos.py proto_files/orc8r/protos proto_files,proto_files/orc8r/protos/prometheus proto_files .
python tools/gen_protos.py proto_files/lte/protos proto_files,proto_files/orc8r/protos/prometheus proto_files .
python tools/gen_prometheus_proto.py . .
```

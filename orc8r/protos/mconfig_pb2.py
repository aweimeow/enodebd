# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: orc8r/protos/mconfig.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='orc8r/protos/mconfig.proto',
  package='magma.orc8r',
  syntax='proto3',
  serialized_options=b'Z\031magma/orc8r/lib/go/protos',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1aorc8r/protos/mconfig.proto\x12\x0bmagma.orc8r\x1a\x19google/protobuf/any.proto\"\xd9\x01\n\x0eGatewayConfigs\x12\x45\n\x0e\x63onfigs_by_key\x18\n \x03(\x0b\x32-.magma.orc8r.GatewayConfigs.ConfigsByKeyEntry\x12\x35\n\x08metadata\x18\x0b \x01(\x0b\x32#.magma.orc8r.GatewayConfigsMetadata\x1aI\n\x11\x43onfigsByKeyEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any:\x02\x38\x01\".\n\x14GatewayConfigsDigest\x12\x16\n\x0emd5_hex_digest\x18\x01 \x01(\t\"_\n\x16GatewayConfigsMetadata\x12\x12\n\ncreated_at\x18\x0b \x01(\x04\x12\x31\n\x06\x64igest\x18\x0c \x01(\x0b\x32!.magma.orc8r.GatewayConfigsDigest\"T\n\x14OffsetGatewayConfigs\x12,\n\x07\x63onfigs\x18\x01 \x01(\x0b\x32\x1b.magma.orc8r.GatewayConfigs\x12\x0e\n\x06offset\x18\x02 \x01(\x03\"&\n\x14MconfigStreamRequest\x12\x0e\n\x06offset\x18\x01 \x01(\x03\x42\x1bZ\x19magma/orc8r/lib/go/protosb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])




_GATEWAYCONFIGS_CONFIGSBYKEYENTRY = _descriptor.Descriptor(
  name='ConfigsByKeyEntry',
  full_name='magma.orc8r.GatewayConfigs.ConfigsByKeyEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='magma.orc8r.GatewayConfigs.ConfigsByKeyEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='magma.orc8r.GatewayConfigs.ConfigsByKeyEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=215,
  serialized_end=288,
)

_GATEWAYCONFIGS = _descriptor.Descriptor(
  name='GatewayConfigs',
  full_name='magma.orc8r.GatewayConfigs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='configs_by_key', full_name='magma.orc8r.GatewayConfigs.configs_by_key', index=0,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='magma.orc8r.GatewayConfigs.metadata', index=1,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_GATEWAYCONFIGS_CONFIGSBYKEYENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=71,
  serialized_end=288,
)


_GATEWAYCONFIGSDIGEST = _descriptor.Descriptor(
  name='GatewayConfigsDigest',
  full_name='magma.orc8r.GatewayConfigsDigest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='md5_hex_digest', full_name='magma.orc8r.GatewayConfigsDigest.md5_hex_digest', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=290,
  serialized_end=336,
)


_GATEWAYCONFIGSMETADATA = _descriptor.Descriptor(
  name='GatewayConfigsMetadata',
  full_name='magma.orc8r.GatewayConfigsMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='created_at', full_name='magma.orc8r.GatewayConfigsMetadata.created_at', index=0,
      number=11, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='digest', full_name='magma.orc8r.GatewayConfigsMetadata.digest', index=1,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=338,
  serialized_end=433,
)


_OFFSETGATEWAYCONFIGS = _descriptor.Descriptor(
  name='OffsetGatewayConfigs',
  full_name='magma.orc8r.OffsetGatewayConfigs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='configs', full_name='magma.orc8r.OffsetGatewayConfigs.configs', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='offset', full_name='magma.orc8r.OffsetGatewayConfigs.offset', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=435,
  serialized_end=519,
)


_MCONFIGSTREAMREQUEST = _descriptor.Descriptor(
  name='MconfigStreamRequest',
  full_name='magma.orc8r.MconfigStreamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='offset', full_name='magma.orc8r.MconfigStreamRequest.offset', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=521,
  serialized_end=559,
)

_GATEWAYCONFIGS_CONFIGSBYKEYENTRY.fields_by_name['value'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_GATEWAYCONFIGS_CONFIGSBYKEYENTRY.containing_type = _GATEWAYCONFIGS
_GATEWAYCONFIGS.fields_by_name['configs_by_key'].message_type = _GATEWAYCONFIGS_CONFIGSBYKEYENTRY
_GATEWAYCONFIGS.fields_by_name['metadata'].message_type = _GATEWAYCONFIGSMETADATA
_GATEWAYCONFIGSMETADATA.fields_by_name['digest'].message_type = _GATEWAYCONFIGSDIGEST
_OFFSETGATEWAYCONFIGS.fields_by_name['configs'].message_type = _GATEWAYCONFIGS
DESCRIPTOR.message_types_by_name['GatewayConfigs'] = _GATEWAYCONFIGS
DESCRIPTOR.message_types_by_name['GatewayConfigsDigest'] = _GATEWAYCONFIGSDIGEST
DESCRIPTOR.message_types_by_name['GatewayConfigsMetadata'] = _GATEWAYCONFIGSMETADATA
DESCRIPTOR.message_types_by_name['OffsetGatewayConfigs'] = _OFFSETGATEWAYCONFIGS
DESCRIPTOR.message_types_by_name['MconfigStreamRequest'] = _MCONFIGSTREAMREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GatewayConfigs = _reflection.GeneratedProtocolMessageType('GatewayConfigs', (_message.Message,), {

  'ConfigsByKeyEntry' : _reflection.GeneratedProtocolMessageType('ConfigsByKeyEntry', (_message.Message,), {
    'DESCRIPTOR' : _GATEWAYCONFIGS_CONFIGSBYKEYENTRY,
    '__module__' : 'orc8r.protos.mconfig_pb2'
    # @@protoc_insertion_point(class_scope:magma.orc8r.GatewayConfigs.ConfigsByKeyEntry)
    })
  ,
  'DESCRIPTOR' : _GATEWAYCONFIGS,
  '__module__' : 'orc8r.protos.mconfig_pb2'
  # @@protoc_insertion_point(class_scope:magma.orc8r.GatewayConfigs)
  })
_sym_db.RegisterMessage(GatewayConfigs)
_sym_db.RegisterMessage(GatewayConfigs.ConfigsByKeyEntry)

GatewayConfigsDigest = _reflection.GeneratedProtocolMessageType('GatewayConfigsDigest', (_message.Message,), {
  'DESCRIPTOR' : _GATEWAYCONFIGSDIGEST,
  '__module__' : 'orc8r.protos.mconfig_pb2'
  # @@protoc_insertion_point(class_scope:magma.orc8r.GatewayConfigsDigest)
  })
_sym_db.RegisterMessage(GatewayConfigsDigest)

GatewayConfigsMetadata = _reflection.GeneratedProtocolMessageType('GatewayConfigsMetadata', (_message.Message,), {
  'DESCRIPTOR' : _GATEWAYCONFIGSMETADATA,
  '__module__' : 'orc8r.protos.mconfig_pb2'
  # @@protoc_insertion_point(class_scope:magma.orc8r.GatewayConfigsMetadata)
  })
_sym_db.RegisterMessage(GatewayConfigsMetadata)

OffsetGatewayConfigs = _reflection.GeneratedProtocolMessageType('OffsetGatewayConfigs', (_message.Message,), {
  'DESCRIPTOR' : _OFFSETGATEWAYCONFIGS,
  '__module__' : 'orc8r.protos.mconfig_pb2'
  # @@protoc_insertion_point(class_scope:magma.orc8r.OffsetGatewayConfigs)
  })
_sym_db.RegisterMessage(OffsetGatewayConfigs)

MconfigStreamRequest = _reflection.GeneratedProtocolMessageType('MconfigStreamRequest', (_message.Message,), {
  'DESCRIPTOR' : _MCONFIGSTREAMREQUEST,
  '__module__' : 'orc8r.protos.mconfig_pb2'
  # @@protoc_insertion_point(class_scope:magma.orc8r.MconfigStreamRequest)
  })
_sym_db.RegisterMessage(MconfigStreamRequest)


DESCRIPTOR._options = None
_GATEWAYCONFIGS_CONFIGSBYKEYENTRY._options = None
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lte/protos/ha_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='lte/protos/ha_service.proto',
  package='magma.lte',
  syntax='proto3',
  serialized_options=b'Z\031magma/lte/cloud/go/protos',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1blte/protos/ha_service.proto\x12\tmagma.lte\"k\n\x16StartAgwOffloadRequest\x12\x0e\n\x06\x65nb_id\x18\x01 \x01(\r\x12\x33\n\x10\x65nb_offload_type\x18\x02 \x01(\x0e\x32\x19.magma.lte.EnbOffloadType\x12\x0c\n\x04imsi\x18\x03 \x01(\t\"\x19\n\x17StartAgwOffloadResponse*C\n\x0e\x45nbOffloadType\x12\x07\n\x03\x41LL\x10\x00\x12\x07\n\x03\x41NY\x10\x01\x12\x11\n\rANY_CONNECTED\x10\x02\x12\x0c\n\x08\x41NY_IDLE\x10\x03\x32g\n\tHaService\x12Z\n\x0fStartAgwOffload\x12!.magma.lte.StartAgwOffloadRequest\x1a\".magma.lte.StartAgwOffloadResponse\"\x00\x42\x1bZ\x19magma/lte/cloud/go/protosb\x06proto3'
)

_ENBOFFLOADTYPE = _descriptor.EnumDescriptor(
  name='EnbOffloadType',
  full_name='magma.lte.EnbOffloadType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ALL', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ANY', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ANY_CONNECTED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ANY_IDLE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=178,
  serialized_end=245,
)
_sym_db.RegisterEnumDescriptor(_ENBOFFLOADTYPE)

EnbOffloadType = enum_type_wrapper.EnumTypeWrapper(_ENBOFFLOADTYPE)
ALL = 0
ANY = 1
ANY_CONNECTED = 2
ANY_IDLE = 3



_STARTAGWOFFLOADREQUEST = _descriptor.Descriptor(
  name='StartAgwOffloadRequest',
  full_name='magma.lte.StartAgwOffloadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='enb_id', full_name='magma.lte.StartAgwOffloadRequest.enb_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enb_offload_type', full_name='magma.lte.StartAgwOffloadRequest.enb_offload_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='imsi', full_name='magma.lte.StartAgwOffloadRequest.imsi', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=42,
  serialized_end=149,
)


_STARTAGWOFFLOADRESPONSE = _descriptor.Descriptor(
  name='StartAgwOffloadResponse',
  full_name='magma.lte.StartAgwOffloadResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=151,
  serialized_end=176,
)

_STARTAGWOFFLOADREQUEST.fields_by_name['enb_offload_type'].enum_type = _ENBOFFLOADTYPE
DESCRIPTOR.message_types_by_name['StartAgwOffloadRequest'] = _STARTAGWOFFLOADREQUEST
DESCRIPTOR.message_types_by_name['StartAgwOffloadResponse'] = _STARTAGWOFFLOADRESPONSE
DESCRIPTOR.enum_types_by_name['EnbOffloadType'] = _ENBOFFLOADTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StartAgwOffloadRequest = _reflection.GeneratedProtocolMessageType('StartAgwOffloadRequest', (_message.Message,), {
  'DESCRIPTOR' : _STARTAGWOFFLOADREQUEST,
  '__module__' : 'lte.protos.ha_service_pb2'
  # @@protoc_insertion_point(class_scope:magma.lte.StartAgwOffloadRequest)
  })
_sym_db.RegisterMessage(StartAgwOffloadRequest)

StartAgwOffloadResponse = _reflection.GeneratedProtocolMessageType('StartAgwOffloadResponse', (_message.Message,), {
  'DESCRIPTOR' : _STARTAGWOFFLOADRESPONSE,
  '__module__' : 'lte.protos.ha_service_pb2'
  # @@protoc_insertion_point(class_scope:magma.lte.StartAgwOffloadResponse)
  })
_sym_db.RegisterMessage(StartAgwOffloadResponse)


DESCRIPTOR._options = None

_HASERVICE = _descriptor.ServiceDescriptor(
  name='HaService',
  full_name='magma.lte.HaService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=247,
  serialized_end=350,
  methods=[
  _descriptor.MethodDescriptor(
    name='StartAgwOffload',
    full_name='magma.lte.HaService.StartAgwOffload',
    index=0,
    containing_service=None,
    input_type=_STARTAGWOFFLOADREQUEST,
    output_type=_STARTAGWOFFLOADRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_HASERVICE)

DESCRIPTOR.services_by_name['HaService'] = _HASERVICE

# @@protoc_insertion_point(module_scope)

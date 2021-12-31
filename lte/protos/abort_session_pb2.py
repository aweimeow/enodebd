# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lte/protos/abort_session.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='lte/protos/abort_session.proto',
  package='magma.lte',
  syntax='proto3',
  serialized_options=b'Z\031magma/lte/cloud/go/protos',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1elte/protos/abort_session.proto\x12\tmagma.lte\"<\n\x13\x41\x62ortSessionRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t\"\xd5\x01\n\x12\x41\x62ortSessionResult\x12\x30\n\x04\x63ode\x18\x01 \x01(\x0e\x32\".magma.lte.AbortSessionResult.Code\x12\x15\n\rerror_message\x18\x02 \x01(\t\"v\n\x04\x43ode\x12\x13\n\x0fSESSION_REMOVED\x10\x00\x12\x15\n\x11SESSION_NOT_FOUND\x10\x01\x12\x12\n\x0eUSER_NOT_FOUND\x10\x02\x12\x15\n\x11GATEWAY_NOT_FOUND\x10\x03\x12\x17\n\x13RADIUS_SERVER_ERROR\x10\x04\x32h\n\x15\x41\x62ortSessionResponder\x12O\n\x0c\x41\x62ortSession\x12\x1e.magma.lte.AbortSessionRequest\x1a\x1d.magma.lte.AbortSessionResult\"\x00\x42\x1bZ\x19magma/lte/cloud/go/protosb\x06proto3'
)



_ABORTSESSIONRESULT_CODE = _descriptor.EnumDescriptor(
  name='Code',
  full_name='magma.lte.AbortSessionResult.Code',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SESSION_REMOVED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SESSION_NOT_FOUND', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='USER_NOT_FOUND', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GATEWAY_NOT_FOUND', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RADIUS_SERVER_ERROR', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=203,
  serialized_end=321,
)
_sym_db.RegisterEnumDescriptor(_ABORTSESSIONRESULT_CODE)


_ABORTSESSIONREQUEST = _descriptor.Descriptor(
  name='AbortSessionRequest',
  full_name='magma.lte.AbortSessionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='magma.lte.AbortSessionRequest.session_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='magma.lte.AbortSessionRequest.user_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=45,
  serialized_end=105,
)


_ABORTSESSIONRESULT = _descriptor.Descriptor(
  name='AbortSessionResult',
  full_name='magma.lte.AbortSessionResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='magma.lte.AbortSessionResult.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_message', full_name='magma.lte.AbortSessionResult.error_message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ABORTSESSIONRESULT_CODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=108,
  serialized_end=321,
)

_ABORTSESSIONRESULT.fields_by_name['code'].enum_type = _ABORTSESSIONRESULT_CODE
_ABORTSESSIONRESULT_CODE.containing_type = _ABORTSESSIONRESULT
DESCRIPTOR.message_types_by_name['AbortSessionRequest'] = _ABORTSESSIONREQUEST
DESCRIPTOR.message_types_by_name['AbortSessionResult'] = _ABORTSESSIONRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AbortSessionRequest = _reflection.GeneratedProtocolMessageType('AbortSessionRequest', (_message.Message,), {
  'DESCRIPTOR' : _ABORTSESSIONREQUEST,
  '__module__' : 'lte.protos.abort_session_pb2'
  # @@protoc_insertion_point(class_scope:magma.lte.AbortSessionRequest)
  })
_sym_db.RegisterMessage(AbortSessionRequest)

AbortSessionResult = _reflection.GeneratedProtocolMessageType('AbortSessionResult', (_message.Message,), {
  'DESCRIPTOR' : _ABORTSESSIONRESULT,
  '__module__' : 'lte.protos.abort_session_pb2'
  # @@protoc_insertion_point(class_scope:magma.lte.AbortSessionResult)
  })
_sym_db.RegisterMessage(AbortSessionResult)


DESCRIPTOR._options = None

_ABORTSESSIONRESPONDER = _descriptor.ServiceDescriptor(
  name='AbortSessionResponder',
  full_name='magma.lte.AbortSessionResponder',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=323,
  serialized_end=427,
  methods=[
  _descriptor.MethodDescriptor(
    name='AbortSession',
    full_name='magma.lte.AbortSessionResponder.AbortSession',
    index=0,
    containing_service=None,
    input_type=_ABORTSESSIONREQUEST,
    output_type=_ABORTSESSIONRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ABORTSESSIONRESPONDER)

DESCRIPTOR.services_by_name['AbortSessionResponder'] = _ABORTSESSIONRESPONDER

# @@protoc_insertion_point(module_scope)

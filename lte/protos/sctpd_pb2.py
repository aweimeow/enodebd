# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lte/protos/sctpd.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='lte/protos/sctpd.proto',
  package='magma.sctpd',
  syntax='proto3',
  serialized_options=b'Z\031magma/lte/cloud/go/protos',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16lte/protos/sctpd.proto\x12\x0bmagma.sctpd\"\x88\x01\n\x07InitReq\x12\x10\n\x08use_ipv4\x18\x01 \x01(\x08\x12\x10\n\x08use_ipv6\x18\x02 \x01(\x08\x12\x12\n\nipv4_addrs\x18\x03 \x03(\t\x12\x12\n\nipv6_addrs\x18\x04 \x03(\t\x12\x0c\n\x04port\x18\x05 \x01(\r\x12\x0c\n\x04ppid\x18\x06 \x01(\r\x12\x15\n\rforce_restart\x18\x07 \x01(\x08\"v\n\x07InitRes\x12/\n\x06result\x18\x01 \x01(\x0e\x32\x1f.magma.sctpd.InitRes.InitResult\":\n\nInitResult\x12\x10\n\x0cINIT_UNKNOWN\x10\x00\x12\x0b\n\x07INIT_OK\x10\x01\x12\r\n\tINIT_FAIL\x10\x02\"L\n\tSendDlReq\x12\x10\n\x08\x61ssoc_id\x18\x01 \x01(\r\x12\x0e\n\x06stream\x18\x02 \x01(\r\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\x12\x0c\n\x04ppid\x18\x04 \x01(\r\"\x87\x01\n\tSendDlRes\x12\x33\n\x06result\x18\x01 \x01(\x0e\x32#.magma.sctpd.SendDlRes.SendDlResult\"E\n\x0cSendDlResult\x12\x13\n\x0fSEND_DL_UNKNOWN\x10\x00\x12\x0e\n\nSEND_DL_OK\x10\x01\x12\x10\n\x0cSEND_DL_FAIL\x10\x02\"L\n\tSendUlReq\x12\x10\n\x08\x61ssoc_id\x18\x01 \x01(\r\x12\x0e\n\x06stream\x18\x02 \x01(\r\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\x12\x0c\n\x04ppid\x18\x04 \x01(\r\"\x0b\n\tSendUlRes\"k\n\x0bNewAssocReq\x12\x10\n\x08\x61ssoc_id\x18\x01 \x01(\r\x12\x11\n\tinstreams\x18\x02 \x01(\r\x12\x12\n\noutstreams\x18\x03 \x01(\r\x12\x15\n\rran_cp_ipaddr\x18\x04 \x01(\x0c\x12\x0c\n\x04ppid\x18\x05 \x01(\r\"\r\n\x0bNewAssocRes\"A\n\rCloseAssocReq\x12\x10\n\x08\x61ssoc_id\x18\x01 \x01(\r\x12\x10\n\x08is_reset\x18\x02 \x01(\x08\x12\x0c\n\x04ppid\x18\x03 \x01(\r\"\x0f\n\rCloseAssocRes2\x81\x01\n\rSctpdDownlink\x12\x34\n\x04Init\x12\x14.magma.sctpd.InitReq\x1a\x14.magma.sctpd.InitRes\"\x00\x12:\n\x06SendDl\x12\x16.magma.sctpd.SendDlReq\x1a\x16.magma.sctpd.SendDlRes\"\x00\x32\xd3\x01\n\x0bSctpdUplink\x12:\n\x06SendUl\x12\x16.magma.sctpd.SendUlReq\x1a\x16.magma.sctpd.SendUlRes\"\x00\x12@\n\x08NewAssoc\x12\x18.magma.sctpd.NewAssocReq\x1a\x18.magma.sctpd.NewAssocRes\"\x00\x12\x46\n\nCloseAssoc\x12\x1a.magma.sctpd.CloseAssocReq\x1a\x1a.magma.sctpd.CloseAssocRes\"\x00\x42\x1bZ\x19magma/lte/cloud/go/protosb\x06proto3'
)



_INITRES_INITRESULT = _descriptor.EnumDescriptor(
  name='InitResult',
  full_name='magma.sctpd.InitRes.InitResult',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INIT_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INIT_OK', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INIT_FAIL', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=238,
  serialized_end=296,
)
_sym_db.RegisterEnumDescriptor(_INITRES_INITRESULT)

_SENDDLRES_SENDDLRESULT = _descriptor.EnumDescriptor(
  name='SendDlResult',
  full_name='magma.sctpd.SendDlRes.SendDlResult',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SEND_DL_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SEND_DL_OK', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SEND_DL_FAIL', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=443,
  serialized_end=512,
)
_sym_db.RegisterEnumDescriptor(_SENDDLRES_SENDDLRESULT)


_INITREQ = _descriptor.Descriptor(
  name='InitReq',
  full_name='magma.sctpd.InitReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='use_ipv4', full_name='magma.sctpd.InitReq.use_ipv4', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='use_ipv6', full_name='magma.sctpd.InitReq.use_ipv6', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ipv4_addrs', full_name='magma.sctpd.InitReq.ipv4_addrs', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ipv6_addrs', full_name='magma.sctpd.InitReq.ipv6_addrs', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='magma.sctpd.InitReq.port', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ppid', full_name='magma.sctpd.InitReq.ppid', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='force_restart', full_name='magma.sctpd.InitReq.force_restart', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=40,
  serialized_end=176,
)


_INITRES = _descriptor.Descriptor(
  name='InitRes',
  full_name='magma.sctpd.InitRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='magma.sctpd.InitRes.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _INITRES_INITRESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=178,
  serialized_end=296,
)


_SENDDLREQ = _descriptor.Descriptor(
  name='SendDlReq',
  full_name='magma.sctpd.SendDlReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='assoc_id', full_name='magma.sctpd.SendDlReq.assoc_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stream', full_name='magma.sctpd.SendDlReq.stream', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload', full_name='magma.sctpd.SendDlReq.payload', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ppid', full_name='magma.sctpd.SendDlReq.ppid', index=3,
      number=4, type=13, cpp_type=3, label=1,
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
  serialized_start=298,
  serialized_end=374,
)


_SENDDLRES = _descriptor.Descriptor(
  name='SendDlRes',
  full_name='magma.sctpd.SendDlRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='magma.sctpd.SendDlRes.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SENDDLRES_SENDDLRESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=377,
  serialized_end=512,
)


_SENDULREQ = _descriptor.Descriptor(
  name='SendUlReq',
  full_name='magma.sctpd.SendUlReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='assoc_id', full_name='magma.sctpd.SendUlReq.assoc_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stream', full_name='magma.sctpd.SendUlReq.stream', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload', full_name='magma.sctpd.SendUlReq.payload', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ppid', full_name='magma.sctpd.SendUlReq.ppid', index=3,
      number=4, type=13, cpp_type=3, label=1,
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
  serialized_start=514,
  serialized_end=590,
)


_SENDULRES = _descriptor.Descriptor(
  name='SendUlRes',
  full_name='magma.sctpd.SendUlRes',
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
  serialized_start=592,
  serialized_end=603,
)


_NEWASSOCREQ = _descriptor.Descriptor(
  name='NewAssocReq',
  full_name='magma.sctpd.NewAssocReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='assoc_id', full_name='magma.sctpd.NewAssocReq.assoc_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='instreams', full_name='magma.sctpd.NewAssocReq.instreams', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='outstreams', full_name='magma.sctpd.NewAssocReq.outstreams', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ran_cp_ipaddr', full_name='magma.sctpd.NewAssocReq.ran_cp_ipaddr', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ppid', full_name='magma.sctpd.NewAssocReq.ppid', index=4,
      number=5, type=13, cpp_type=3, label=1,
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
  serialized_start=605,
  serialized_end=712,
)


_NEWASSOCRES = _descriptor.Descriptor(
  name='NewAssocRes',
  full_name='magma.sctpd.NewAssocRes',
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
  serialized_start=714,
  serialized_end=727,
)


_CLOSEASSOCREQ = _descriptor.Descriptor(
  name='CloseAssocReq',
  full_name='magma.sctpd.CloseAssocReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='assoc_id', full_name='magma.sctpd.CloseAssocReq.assoc_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_reset', full_name='magma.sctpd.CloseAssocReq.is_reset', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ppid', full_name='magma.sctpd.CloseAssocReq.ppid', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  serialized_start=729,
  serialized_end=794,
)


_CLOSEASSOCRES = _descriptor.Descriptor(
  name='CloseAssocRes',
  full_name='magma.sctpd.CloseAssocRes',
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
  serialized_start=796,
  serialized_end=811,
)

_INITRES.fields_by_name['result'].enum_type = _INITRES_INITRESULT
_INITRES_INITRESULT.containing_type = _INITRES
_SENDDLRES.fields_by_name['result'].enum_type = _SENDDLRES_SENDDLRESULT
_SENDDLRES_SENDDLRESULT.containing_type = _SENDDLRES
DESCRIPTOR.message_types_by_name['InitReq'] = _INITREQ
DESCRIPTOR.message_types_by_name['InitRes'] = _INITRES
DESCRIPTOR.message_types_by_name['SendDlReq'] = _SENDDLREQ
DESCRIPTOR.message_types_by_name['SendDlRes'] = _SENDDLRES
DESCRIPTOR.message_types_by_name['SendUlReq'] = _SENDULREQ
DESCRIPTOR.message_types_by_name['SendUlRes'] = _SENDULRES
DESCRIPTOR.message_types_by_name['NewAssocReq'] = _NEWASSOCREQ
DESCRIPTOR.message_types_by_name['NewAssocRes'] = _NEWASSOCRES
DESCRIPTOR.message_types_by_name['CloseAssocReq'] = _CLOSEASSOCREQ
DESCRIPTOR.message_types_by_name['CloseAssocRes'] = _CLOSEASSOCRES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InitReq = _reflection.GeneratedProtocolMessageType('InitReq', (_message.Message,), {
  'DESCRIPTOR' : _INITREQ,
  '__module__' : 'lte.protos.sctpd_pb2'
  # @@protoc_insertion_point(class_scope:magma.sctpd.InitReq)
  })
_sym_db.RegisterMessage(InitReq)

InitRes = _reflection.GeneratedProtocolMessageType('InitRes', (_message.Message,), {
  'DESCRIPTOR' : _INITRES,
  '__module__' : 'lte.protos.sctpd_pb2'
  # @@protoc_insertion_point(class_scope:magma.sctpd.InitRes)
  })
_sym_db.RegisterMessage(InitRes)

SendDlReq = _reflection.GeneratedProtocolMessageType('SendDlReq', (_message.Message,), {
  'DESCRIPTOR' : _SENDDLREQ,
  '__module__' : 'lte.protos.sctpd_pb2'
  # @@protoc_insertion_point(class_scope:magma.sctpd.SendDlReq)
  })
_sym_db.RegisterMessage(SendDlReq)

SendDlRes = _reflection.GeneratedProtocolMessageType('SendDlRes', (_message.Message,), {
  'DESCRIPTOR' : _SENDDLRES,
  '__module__' : 'lte.protos.sctpd_pb2'
  # @@protoc_insertion_point(class_scope:magma.sctpd.SendDlRes)
  })
_sym_db.RegisterMessage(SendDlRes)

SendUlReq = _reflection.GeneratedProtocolMessageType('SendUlReq', (_message.Message,), {
  'DESCRIPTOR' : _SENDULREQ,
  '__module__' : 'lte.protos.sctpd_pb2'
  # @@protoc_insertion_point(class_scope:magma.sctpd.SendUlReq)
  })
_sym_db.RegisterMessage(SendUlReq)

SendUlRes = _reflection.GeneratedProtocolMessageType('SendUlRes', (_message.Message,), {
  'DESCRIPTOR' : _SENDULRES,
  '__module__' : 'lte.protos.sctpd_pb2'
  # @@protoc_insertion_point(class_scope:magma.sctpd.SendUlRes)
  })
_sym_db.RegisterMessage(SendUlRes)

NewAssocReq = _reflection.GeneratedProtocolMessageType('NewAssocReq', (_message.Message,), {
  'DESCRIPTOR' : _NEWASSOCREQ,
  '__module__' : 'lte.protos.sctpd_pb2'
  # @@protoc_insertion_point(class_scope:magma.sctpd.NewAssocReq)
  })
_sym_db.RegisterMessage(NewAssocReq)

NewAssocRes = _reflection.GeneratedProtocolMessageType('NewAssocRes', (_message.Message,), {
  'DESCRIPTOR' : _NEWASSOCRES,
  '__module__' : 'lte.protos.sctpd_pb2'
  # @@protoc_insertion_point(class_scope:magma.sctpd.NewAssocRes)
  })
_sym_db.RegisterMessage(NewAssocRes)

CloseAssocReq = _reflection.GeneratedProtocolMessageType('CloseAssocReq', (_message.Message,), {
  'DESCRIPTOR' : _CLOSEASSOCREQ,
  '__module__' : 'lte.protos.sctpd_pb2'
  # @@protoc_insertion_point(class_scope:magma.sctpd.CloseAssocReq)
  })
_sym_db.RegisterMessage(CloseAssocReq)

CloseAssocRes = _reflection.GeneratedProtocolMessageType('CloseAssocRes', (_message.Message,), {
  'DESCRIPTOR' : _CLOSEASSOCRES,
  '__module__' : 'lte.protos.sctpd_pb2'
  # @@protoc_insertion_point(class_scope:magma.sctpd.CloseAssocRes)
  })
_sym_db.RegisterMessage(CloseAssocRes)


DESCRIPTOR._options = None

_SCTPDDOWNLINK = _descriptor.ServiceDescriptor(
  name='SctpdDownlink',
  full_name='magma.sctpd.SctpdDownlink',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=814,
  serialized_end=943,
  methods=[
  _descriptor.MethodDescriptor(
    name='Init',
    full_name='magma.sctpd.SctpdDownlink.Init',
    index=0,
    containing_service=None,
    input_type=_INITREQ,
    output_type=_INITRES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SendDl',
    full_name='magma.sctpd.SctpdDownlink.SendDl',
    index=1,
    containing_service=None,
    input_type=_SENDDLREQ,
    output_type=_SENDDLRES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SCTPDDOWNLINK)

DESCRIPTOR.services_by_name['SctpdDownlink'] = _SCTPDDOWNLINK


_SCTPDUPLINK = _descriptor.ServiceDescriptor(
  name='SctpdUplink',
  full_name='magma.sctpd.SctpdUplink',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=946,
  serialized_end=1157,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendUl',
    full_name='magma.sctpd.SctpdUplink.SendUl',
    index=0,
    containing_service=None,
    input_type=_SENDULREQ,
    output_type=_SENDULRES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='NewAssoc',
    full_name='magma.sctpd.SctpdUplink.NewAssoc',
    index=1,
    containing_service=None,
    input_type=_NEWASSOCREQ,
    output_type=_NEWASSOCRES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CloseAssoc',
    full_name='magma.sctpd.SctpdUplink.CloseAssoc',
    index=2,
    containing_service=None,
    input_type=_CLOSEASSOCREQ,
    output_type=_CLOSEASSOCRES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SCTPDUPLINK)

DESCRIPTOR.services_by_name['SctpdUplink'] = _SCTPDUPLINK

# @@protoc_insertion_point(module_scope)

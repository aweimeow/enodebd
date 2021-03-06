# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lte/protos/subscriberauth.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='lte/protos/subscriberauth.proto',
  package='magma.lte',
  syntax='proto3',
  serialized_options=b'Z\031magma/lte/cloud/go/protos',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1flte/protos/subscriberauth.proto\x12\tmagma.lte\"k\n#M5GAuthenticationInformationRequest\x12\x11\n\tuser_name\x18\x01 \x01(\t\x12\x13\n\x0bresync_info\x18\x02 \x01(\x0c\x12\x1c\n\x14serving_network_name\x18\x03 \x01(\t\"\x8a\x02\n\"M5GAuthenticationInformationAnswer\x12+\n\nerror_code\x18\x01 \x01(\x0e\x32\x17.magma.lte.M5GErrorCode\x12^\n\x0fm5gauth_vectors\x18\x02 \x03(\x0b\x32\x45.magma.lte.M5GAuthenticationInformationAnswer.M5GAuthenticationVector\x1aW\n\x17M5GAuthenticationVector\x12\x0c\n\x04rand\x18\x01 \x01(\x0c\x12\x11\n\txres_star\x18\x02 \x01(\x0c\x12\x0c\n\x04\x61utn\x18\x03 \x01(\x0c\x12\r\n\x05kseaf\x18\x04 \x01(\x0c*\xf2\x04\n\x0cM5GErrorCode\x12\r\n\tUNDEFINED\x10\x00\x12\x15\n\x10MULTI_ROUND_AUTH\x10\xe9\x07\x12\x0c\n\x07SUCCESS\x10\xd1\x0f\x12\x14\n\x0fLIMITED_SUCCESS\x10\xd2\x0f\x12\x17\n\x12\x43OMMAND_UNSUPORTED\x10\xb9\x17\x12\x16\n\x11UNABLE_TO_DELIVER\x10\xba\x17\x12\x15\n\x10REALM_NOT_SERVED\x10\xbb\x17\x12\r\n\x08TOO_BUSY\x10\xbc\x17\x12\x12\n\rLOOP_DETECTED\x10\xbd\x17\x12\x18\n\x13REDIRECT_INDICATION\x10\xbe\x17\x12\x1c\n\x17\x41PPLICATION_UNSUPPORTED\x10\xbf\x17\x12\x15\n\x10INVALIDH_DR_BITS\x10\xc0\x17\x12\x15\n\x10INVALID_AVP_BITS\x10\xc1\x17\x12\x11\n\x0cUNKNOWN_PEER\x10\xc2\x17\x12\x1c\n\x17\x41UTHENTICATION_REJECTED\x10\xa1\x1f\x12\x11\n\x0cOUT_OF_SPACE\x10\xa2\x1f\x12\x12\n\rELECTION_LOST\x10\xa3\x1f\x12\x1b\n\x16\x41UTHORIZATION_REJECTED\x10\x8b\'\x12\x11\n\x0cUSER_UNKNOWN\x10\x89\'\x12\x17\n\x12UNKNOWN_SESSION_ID\x10\x8a\'\x12\x1d\n\x18UNKNOWN_EPS_SUBSCRIPTION\x10\xac*\x12\x14\n\x0fRAT_NOT_ALLOWED\x10\xad*\x12\x18\n\x13ROAMING_NOT_ALLOWED\x10\x8c\'\x12\x16\n\x11\x45QUIPMENT_UNKNOWN\x10\xae*\x12\x19\n\x14UNKNOWN_SERVING_NODE\x10\xaf*\x12$\n\x1f\x41UTHENTICATION_DATA_UNAVAILABLE\x10\xd5 2\x9e\x01\n\x1bM5GSubscriberAuthentication\x12\x7f\n\x1cM5GAuthenticationInformation\x12..magma.lte.M5GAuthenticationInformationRequest\x1a-.magma.lte.M5GAuthenticationInformationAnswer\"\x00\x42\x1bZ\x19magma/lte/cloud/go/protosb\x06proto3'
)

_M5GERRORCODE = _descriptor.EnumDescriptor(
  name='M5GErrorCode',
  full_name='magma.lte.M5GErrorCode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MULTI_ROUND_AUTH', index=1, number=1001,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=2, number=2001,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LIMITED_SUCCESS', index=3, number=2002,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COMMAND_UNSUPORTED', index=4, number=3001,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNABLE_TO_DELIVER', index=5, number=3002,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REALM_NOT_SERVED', index=6, number=3003,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TOO_BUSY', index=7, number=3004,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LOOP_DETECTED', index=8, number=3005,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REDIRECT_INDICATION', index=9, number=3006,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='APPLICATION_UNSUPPORTED', index=10, number=3007,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALIDH_DR_BITS', index=11, number=3008,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_AVP_BITS', index=12, number=3009,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_PEER', index=13, number=3010,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AUTHENTICATION_REJECTED', index=14, number=4001,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OUT_OF_SPACE', index=15, number=4002,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ELECTION_LOST', index=16, number=4003,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AUTHORIZATION_REJECTED', index=17, number=5003,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='USER_UNKNOWN', index=18, number=5001,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_SESSION_ID', index=19, number=5002,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_EPS_SUBSCRIPTION', index=20, number=5420,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RAT_NOT_ALLOWED', index=21, number=5421,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ROAMING_NOT_ALLOWED', index=22, number=5004,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EQUIPMENT_UNKNOWN', index=23, number=5422,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_SERVING_NODE', index=24, number=5423,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AUTHENTICATION_DATA_UNAVAILABLE', index=25, number=4181,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=425,
  serialized_end=1051,
)
_sym_db.RegisterEnumDescriptor(_M5GERRORCODE)

M5GErrorCode = enum_type_wrapper.EnumTypeWrapper(_M5GERRORCODE)
UNDEFINED = 0
MULTI_ROUND_AUTH = 1001
SUCCESS = 2001
LIMITED_SUCCESS = 2002
COMMAND_UNSUPORTED = 3001
UNABLE_TO_DELIVER = 3002
REALM_NOT_SERVED = 3003
TOO_BUSY = 3004
LOOP_DETECTED = 3005
REDIRECT_INDICATION = 3006
APPLICATION_UNSUPPORTED = 3007
INVALIDH_DR_BITS = 3008
INVALID_AVP_BITS = 3009
UNKNOWN_PEER = 3010
AUTHENTICATION_REJECTED = 4001
OUT_OF_SPACE = 4002
ELECTION_LOST = 4003
AUTHORIZATION_REJECTED = 5003
USER_UNKNOWN = 5001
UNKNOWN_SESSION_ID = 5002
UNKNOWN_EPS_SUBSCRIPTION = 5420
RAT_NOT_ALLOWED = 5421
ROAMING_NOT_ALLOWED = 5004
EQUIPMENT_UNKNOWN = 5422
UNKNOWN_SERVING_NODE = 5423
AUTHENTICATION_DATA_UNAVAILABLE = 4181



_M5GAUTHENTICATIONINFORMATIONREQUEST = _descriptor.Descriptor(
  name='M5GAuthenticationInformationRequest',
  full_name='magma.lte.M5GAuthenticationInformationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_name', full_name='magma.lte.M5GAuthenticationInformationRequest.user_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resync_info', full_name='magma.lte.M5GAuthenticationInformationRequest.resync_info', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serving_network_name', full_name='magma.lte.M5GAuthenticationInformationRequest.serving_network_name', index=2,
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
  serialized_start=46,
  serialized_end=153,
)


_M5GAUTHENTICATIONINFORMATIONANSWER_M5GAUTHENTICATIONVECTOR = _descriptor.Descriptor(
  name='M5GAuthenticationVector',
  full_name='magma.lte.M5GAuthenticationInformationAnswer.M5GAuthenticationVector',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rand', full_name='magma.lte.M5GAuthenticationInformationAnswer.M5GAuthenticationVector.rand', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='xres_star', full_name='magma.lte.M5GAuthenticationInformationAnswer.M5GAuthenticationVector.xres_star', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='autn', full_name='magma.lte.M5GAuthenticationInformationAnswer.M5GAuthenticationVector.autn', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='kseaf', full_name='magma.lte.M5GAuthenticationInformationAnswer.M5GAuthenticationVector.kseaf', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=335,
  serialized_end=422,
)

_M5GAUTHENTICATIONINFORMATIONANSWER = _descriptor.Descriptor(
  name='M5GAuthenticationInformationAnswer',
  full_name='magma.lte.M5GAuthenticationInformationAnswer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_code', full_name='magma.lte.M5GAuthenticationInformationAnswer.error_code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='m5gauth_vectors', full_name='magma.lte.M5GAuthenticationInformationAnswer.m5gauth_vectors', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_M5GAUTHENTICATIONINFORMATIONANSWER_M5GAUTHENTICATIONVECTOR, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=156,
  serialized_end=422,
)

_M5GAUTHENTICATIONINFORMATIONANSWER_M5GAUTHENTICATIONVECTOR.containing_type = _M5GAUTHENTICATIONINFORMATIONANSWER
_M5GAUTHENTICATIONINFORMATIONANSWER.fields_by_name['error_code'].enum_type = _M5GERRORCODE
_M5GAUTHENTICATIONINFORMATIONANSWER.fields_by_name['m5gauth_vectors'].message_type = _M5GAUTHENTICATIONINFORMATIONANSWER_M5GAUTHENTICATIONVECTOR
DESCRIPTOR.message_types_by_name['M5GAuthenticationInformationRequest'] = _M5GAUTHENTICATIONINFORMATIONREQUEST
DESCRIPTOR.message_types_by_name['M5GAuthenticationInformationAnswer'] = _M5GAUTHENTICATIONINFORMATIONANSWER
DESCRIPTOR.enum_types_by_name['M5GErrorCode'] = _M5GERRORCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

M5GAuthenticationInformationRequest = _reflection.GeneratedProtocolMessageType('M5GAuthenticationInformationRequest', (_message.Message,), {
  'DESCRIPTOR' : _M5GAUTHENTICATIONINFORMATIONREQUEST,
  '__module__' : 'lte.protos.subscriberauth_pb2'
  # @@protoc_insertion_point(class_scope:magma.lte.M5GAuthenticationInformationRequest)
  })
_sym_db.RegisterMessage(M5GAuthenticationInformationRequest)

M5GAuthenticationInformationAnswer = _reflection.GeneratedProtocolMessageType('M5GAuthenticationInformationAnswer', (_message.Message,), {

  'M5GAuthenticationVector' : _reflection.GeneratedProtocolMessageType('M5GAuthenticationVector', (_message.Message,), {
    'DESCRIPTOR' : _M5GAUTHENTICATIONINFORMATIONANSWER_M5GAUTHENTICATIONVECTOR,
    '__module__' : 'lte.protos.subscriberauth_pb2'
    # @@protoc_insertion_point(class_scope:magma.lte.M5GAuthenticationInformationAnswer.M5GAuthenticationVector)
    })
  ,
  'DESCRIPTOR' : _M5GAUTHENTICATIONINFORMATIONANSWER,
  '__module__' : 'lte.protos.subscriberauth_pb2'
  # @@protoc_insertion_point(class_scope:magma.lte.M5GAuthenticationInformationAnswer)
  })
_sym_db.RegisterMessage(M5GAuthenticationInformationAnswer)
_sym_db.RegisterMessage(M5GAuthenticationInformationAnswer.M5GAuthenticationVector)


DESCRIPTOR._options = None

_M5GSUBSCRIBERAUTHENTICATION = _descriptor.ServiceDescriptor(
  name='M5GSubscriberAuthentication',
  full_name='magma.lte.M5GSubscriberAuthentication',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1054,
  serialized_end=1212,
  methods=[
  _descriptor.MethodDescriptor(
    name='M5GAuthenticationInformation',
    full_name='magma.lte.M5GSubscriberAuthentication.M5GAuthenticationInformation',
    index=0,
    containing_service=None,
    input_type=_M5GAUTHENTICATIONINFORMATIONREQUEST,
    output_type=_M5GAUTHENTICATIONINFORMATIONANSWER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_M5GSUBSCRIBERAUTHENTICATION)

DESCRIPTOR.services_by_name['M5GSubscriberAuthentication'] = _M5GSUBSCRIBERAUTHENTICATION

# @@protoc_insertion_point(module_scope)

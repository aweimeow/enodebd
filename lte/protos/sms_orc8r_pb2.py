# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lte/protos/sms_orc8r.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from orc8r.protos import common_pb2 as orc8r_dot_protos_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='lte/protos/sms_orc8r.proto',
  package='magma.lte',
  syntax='proto3',
  serialized_options=b'Z\031magma/lte/cloud/go/protos',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1alte/protos/sms_orc8r.proto\x12\tmagma.lte\x1a\x19orc8r/protos/common.proto\"B\n\x13SMODownlinkUnitdata\x12\x0c\n\x04imsi\x18\x01 \x01(\t\x12\x1d\n\x15nas_message_container\x18\x02 \x01(\x0c\"\xa5\x01\n\x11SMOUplinkUnitdata\x12\x0c\n\x04imsi\x18\x01 \x01(\t\x12\x1d\n\x15nas_message_container\x18\x02 \x01(\x0c\x12\x0e\n\x06imeisv\x18\x03 \x01(\x0c\x12\x14\n\x0cue_time_zone\x18\x04 \x01(\x0c\x12!\n\x19mobile_station_classmark2\x18\x05 \x01(\x0c\x12\x0b\n\x03tai\x18\x06 \x01(\x0c\x12\r\n\x05\x65_cgi\x18\x07 \x01(\x0c\"\x18\n\x16ReportDeliveryResponse\"E\n\x15ReportDeliveryRequest\x12,\n\x06report\x18\x01 \x01(\x0b\x32\x1c.magma.lte.SMOUplinkUnitdata\"#\n\x12GetMessagesRequest\x12\r\n\x05imsis\x18\x01 \x03(\t\"G\n\x13GetMessagesResponse\x12\x30\n\x08messages\x18\x01 \x03(\x0b\x32\x1e.magma.lte.SMODownlinkUnitdata2Q\n\x0fSMSOrc8rService\x12>\n\tSMOUplink\x12\x1c.magma.lte.SMOUplinkUnitdata\x1a\x11.magma.orc8r.Void\"\x00\x32\\\n\x16SMSOrc8rGatewayService\x12\x42\n\x0bSMODownlink\x12\x1e.magma.lte.SMODownlinkUnitdata\x1a\x11.magma.orc8r.Void\"\x00\x32\xaf\x01\n\x04SmsD\x12W\n\x0eReportDelivery\x12 .magma.lte.ReportDeliveryRequest\x1a!.magma.lte.ReportDeliveryResponse\"\x00\x12N\n\x0bGetMessages\x12\x1d.magma.lte.GetMessagesRequest\x1a\x1e.magma.lte.GetMessagesResponse\"\x00\x42\x1bZ\x19magma/lte/cloud/go/protosb\x06proto3'
  ,
  dependencies=[orc8r_dot_protos_dot_common__pb2.DESCRIPTOR,])




_SMODOWNLINKUNITDATA = _descriptor.Descriptor(
  name='SMODownlinkUnitdata',
  full_name='magma.lte.SMODownlinkUnitdata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='imsi', full_name='magma.lte.SMODownlinkUnitdata.imsi', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nas_message_container', full_name='magma.lte.SMODownlinkUnitdata.nas_message_container', index=1,
      number=2, type=12, cpp_type=9, label=1,
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
  serialized_start=68,
  serialized_end=134,
)


_SMOUPLINKUNITDATA = _descriptor.Descriptor(
  name='SMOUplinkUnitdata',
  full_name='magma.lte.SMOUplinkUnitdata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='imsi', full_name='magma.lte.SMOUplinkUnitdata.imsi', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nas_message_container', full_name='magma.lte.SMOUplinkUnitdata.nas_message_container', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='imeisv', full_name='magma.lte.SMOUplinkUnitdata.imeisv', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ue_time_zone', full_name='magma.lte.SMOUplinkUnitdata.ue_time_zone', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mobile_station_classmark2', full_name='magma.lte.SMOUplinkUnitdata.mobile_station_classmark2', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tai', full_name='magma.lte.SMOUplinkUnitdata.tai', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='e_cgi', full_name='magma.lte.SMOUplinkUnitdata.e_cgi', index=6,
      number=7, type=12, cpp_type=9, label=1,
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
  serialized_start=137,
  serialized_end=302,
)


_REPORTDELIVERYRESPONSE = _descriptor.Descriptor(
  name='ReportDeliveryResponse',
  full_name='magma.lte.ReportDeliveryResponse',
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
  serialized_start=304,
  serialized_end=328,
)


_REPORTDELIVERYREQUEST = _descriptor.Descriptor(
  name='ReportDeliveryRequest',
  full_name='magma.lte.ReportDeliveryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='report', full_name='magma.lte.ReportDeliveryRequest.report', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=330,
  serialized_end=399,
)


_GETMESSAGESREQUEST = _descriptor.Descriptor(
  name='GetMessagesRequest',
  full_name='magma.lte.GetMessagesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='imsis', full_name='magma.lte.GetMessagesRequest.imsis', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=401,
  serialized_end=436,
)


_GETMESSAGESRESPONSE = _descriptor.Descriptor(
  name='GetMessagesResponse',
  full_name='magma.lte.GetMessagesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='messages', full_name='magma.lte.GetMessagesResponse.messages', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=438,
  serialized_end=509,
)

_REPORTDELIVERYREQUEST.fields_by_name['report'].message_type = _SMOUPLINKUNITDATA
_GETMESSAGESRESPONSE.fields_by_name['messages'].message_type = _SMODOWNLINKUNITDATA
DESCRIPTOR.message_types_by_name['SMODownlinkUnitdata'] = _SMODOWNLINKUNITDATA
DESCRIPTOR.message_types_by_name['SMOUplinkUnitdata'] = _SMOUPLINKUNITDATA
DESCRIPTOR.message_types_by_name['ReportDeliveryResponse'] = _REPORTDELIVERYRESPONSE
DESCRIPTOR.message_types_by_name['ReportDeliveryRequest'] = _REPORTDELIVERYREQUEST
DESCRIPTOR.message_types_by_name['GetMessagesRequest'] = _GETMESSAGESREQUEST
DESCRIPTOR.message_types_by_name['GetMessagesResponse'] = _GETMESSAGESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SMODownlinkUnitdata = _reflection.GeneratedProtocolMessageType('SMODownlinkUnitdata', (_message.Message,), {
  'DESCRIPTOR' : _SMODOWNLINKUNITDATA,
  '__module__' : 'lte.protos.sms_orc8r_pb2'
  # @@protoc_insertion_point(class_scope:magma.lte.SMODownlinkUnitdata)
  })
_sym_db.RegisterMessage(SMODownlinkUnitdata)

SMOUplinkUnitdata = _reflection.GeneratedProtocolMessageType('SMOUplinkUnitdata', (_message.Message,), {
  'DESCRIPTOR' : _SMOUPLINKUNITDATA,
  '__module__' : 'lte.protos.sms_orc8r_pb2'
  # @@protoc_insertion_point(class_scope:magma.lte.SMOUplinkUnitdata)
  })
_sym_db.RegisterMessage(SMOUplinkUnitdata)

ReportDeliveryResponse = _reflection.GeneratedProtocolMessageType('ReportDeliveryResponse', (_message.Message,), {
  'DESCRIPTOR' : _REPORTDELIVERYRESPONSE,
  '__module__' : 'lte.protos.sms_orc8r_pb2'
  # @@protoc_insertion_point(class_scope:magma.lte.ReportDeliveryResponse)
  })
_sym_db.RegisterMessage(ReportDeliveryResponse)

ReportDeliveryRequest = _reflection.GeneratedProtocolMessageType('ReportDeliveryRequest', (_message.Message,), {
  'DESCRIPTOR' : _REPORTDELIVERYREQUEST,
  '__module__' : 'lte.protos.sms_orc8r_pb2'
  # @@protoc_insertion_point(class_scope:magma.lte.ReportDeliveryRequest)
  })
_sym_db.RegisterMessage(ReportDeliveryRequest)

GetMessagesRequest = _reflection.GeneratedProtocolMessageType('GetMessagesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETMESSAGESREQUEST,
  '__module__' : 'lte.protos.sms_orc8r_pb2'
  # @@protoc_insertion_point(class_scope:magma.lte.GetMessagesRequest)
  })
_sym_db.RegisterMessage(GetMessagesRequest)

GetMessagesResponse = _reflection.GeneratedProtocolMessageType('GetMessagesResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETMESSAGESRESPONSE,
  '__module__' : 'lte.protos.sms_orc8r_pb2'
  # @@protoc_insertion_point(class_scope:magma.lte.GetMessagesResponse)
  })
_sym_db.RegisterMessage(GetMessagesResponse)


DESCRIPTOR._options = None

_SMSORC8RSERVICE = _descriptor.ServiceDescriptor(
  name='SMSOrc8rService',
  full_name='magma.lte.SMSOrc8rService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=511,
  serialized_end=592,
  methods=[
  _descriptor.MethodDescriptor(
    name='SMOUplink',
    full_name='magma.lte.SMSOrc8rService.SMOUplink',
    index=0,
    containing_service=None,
    input_type=_SMOUPLINKUNITDATA,
    output_type=orc8r_dot_protos_dot_common__pb2._VOID,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SMSORC8RSERVICE)

DESCRIPTOR.services_by_name['SMSOrc8rService'] = _SMSORC8RSERVICE


_SMSORC8RGATEWAYSERVICE = _descriptor.ServiceDescriptor(
  name='SMSOrc8rGatewayService',
  full_name='magma.lte.SMSOrc8rGatewayService',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=594,
  serialized_end=686,
  methods=[
  _descriptor.MethodDescriptor(
    name='SMODownlink',
    full_name='magma.lte.SMSOrc8rGatewayService.SMODownlink',
    index=0,
    containing_service=None,
    input_type=_SMODOWNLINKUNITDATA,
    output_type=orc8r_dot_protos_dot_common__pb2._VOID,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SMSORC8RGATEWAYSERVICE)

DESCRIPTOR.services_by_name['SMSOrc8rGatewayService'] = _SMSORC8RGATEWAYSERVICE


_SMSD = _descriptor.ServiceDescriptor(
  name='SmsD',
  full_name='magma.lte.SmsD',
  file=DESCRIPTOR,
  index=2,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=689,
  serialized_end=864,
  methods=[
  _descriptor.MethodDescriptor(
    name='ReportDelivery',
    full_name='magma.lte.SmsD.ReportDelivery',
    index=0,
    containing_service=None,
    input_type=_REPORTDELIVERYREQUEST,
    output_type=_REPORTDELIVERYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetMessages',
    full_name='magma.lte.SmsD.GetMessages',
    index=1,
    containing_service=None,
    input_type=_GETMESSAGESREQUEST,
    output_type=_GETMESSAGESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SMSD)

DESCRIPTOR.services_by_name['SmsD'] = _SMSD

# @@protoc_insertion_point(module_scope)

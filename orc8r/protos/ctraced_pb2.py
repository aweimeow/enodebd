# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: orc8r/protos/ctraced.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='orc8r/protos/ctraced.proto',
  package='magma.orc8r',
  syntax='proto3',
  serialized_options=b'Z\031magma/orc8r/lib/go/protos',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1aorc8r/protos/ctraced.proto\x12\x0bmagma.orc8r\"\xd6\x03\n\x11StartTraceRequest\x12\x10\n\x08trace_id\x18\x08 \x01(\t\x12<\n\ntrace_type\x18\x01 \x01(\x0e\x32(.magma.orc8r.StartTraceRequest.TraceType\x12\x0c\n\x04imsi\x18\x02 \x01(\t\x12=\n\x08protocol\x18\x03 \x01(\x0e\x32+.magma.orc8r.StartTraceRequest.ProtocolName\x12?\n\tinterface\x18\x04 \x01(\x0e\x32,.magma.orc8r.StartTraceRequest.InterfaceName\x12\x0f\n\x07timeout\x18\x05 \x01(\r\x12\x17\n\x0f\x63\x61pture_filters\x18\x06 \x01(\t\x12\x17\n\x0f\x64isplay_filters\x18\x07 \x01(\t\"M\n\tTraceType\x12\x07\n\x03\x41LL\x10\x00\x12\x0e\n\nSUBSCRIBER\x10\x01\x12\x0c\n\x08PROTOCOL\x10\x02\x12\r\n\tINTERFACE\x10\x03\x12\n\n\x06\x43USTOM\x10\x04\"&\n\x0cProtocolName\x12\x08\n\x04SCTP\x10\x00\x12\x0c\n\x08\x44IAMETER\x10\x01\")\n\rInterfaceName\x12\x08\n\x04S1AP\x10\x00\x12\x06\n\x02GX\x10\x01\x12\x06\n\x02GT\x10\x02\"%\n\x12StartTraceResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"#\n\x0f\x45ndTraceRequest\x12\x10\n\x08trace_id\x18\x01 \x01(\t\":\n\x10\x45ndTraceResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x15\n\rtrace_content\x18\x02 \x01(\x0c\"S\n\x17ReportEndedTraceRequest\x12\x10\n\x08trace_id\x18\x01 \x01(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\x12\x15\n\rtrace_content\x18\x03 \x01(\x0c\"\x1a\n\x18ReportEndedTraceResponse2\xb6\x01\n\x10\x43\x61llTraceService\x12S\n\x0eStartCallTrace\x12\x1e.magma.orc8r.StartTraceRequest\x1a\x1f.magma.orc8r.StartTraceResponse\"\x00\x12M\n\x0c\x45ndCallTrace\x12\x1c.magma.orc8r.EndTraceRequest\x1a\x1d.magma.orc8r.EndTraceResponse\"\x00\x32|\n\x13\x43\x61llTraceController\x12\x65\n\x14ReportEndedCallTrace\x12$.magma.orc8r.ReportEndedTraceRequest\x1a%.magma.orc8r.ReportEndedTraceResponse\"\x00\x42\x1bZ\x19magma/orc8r/lib/go/protosb\x06proto3'
)



_STARTTRACEREQUEST_TRACETYPE = _descriptor.EnumDescriptor(
  name='TraceType',
  full_name='magma.orc8r.StartTraceRequest.TraceType',
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
      name='SUBSCRIBER', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PROTOCOL', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INTERFACE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=354,
  serialized_end=431,
)
_sym_db.RegisterEnumDescriptor(_STARTTRACEREQUEST_TRACETYPE)

_STARTTRACEREQUEST_PROTOCOLNAME = _descriptor.EnumDescriptor(
  name='ProtocolName',
  full_name='magma.orc8r.StartTraceRequest.ProtocolName',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SCTP', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DIAMETER', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=433,
  serialized_end=471,
)
_sym_db.RegisterEnumDescriptor(_STARTTRACEREQUEST_PROTOCOLNAME)

_STARTTRACEREQUEST_INTERFACENAME = _descriptor.EnumDescriptor(
  name='InterfaceName',
  full_name='magma.orc8r.StartTraceRequest.InterfaceName',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='S1AP', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GX', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GT', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=473,
  serialized_end=514,
)
_sym_db.RegisterEnumDescriptor(_STARTTRACEREQUEST_INTERFACENAME)


_STARTTRACEREQUEST = _descriptor.Descriptor(
  name='StartTraceRequest',
  full_name='magma.orc8r.StartTraceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='trace_id', full_name='magma.orc8r.StartTraceRequest.trace_id', index=0,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trace_type', full_name='magma.orc8r.StartTraceRequest.trace_type', index=1,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='imsi', full_name='magma.orc8r.StartTraceRequest.imsi', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='protocol', full_name='magma.orc8r.StartTraceRequest.protocol', index=3,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='interface', full_name='magma.orc8r.StartTraceRequest.interface', index=4,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='magma.orc8r.StartTraceRequest.timeout', index=5,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='capture_filters', full_name='magma.orc8r.StartTraceRequest.capture_filters', index=6,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='display_filters', full_name='magma.orc8r.StartTraceRequest.display_filters', index=7,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STARTTRACEREQUEST_TRACETYPE,
    _STARTTRACEREQUEST_PROTOCOLNAME,
    _STARTTRACEREQUEST_INTERFACENAME,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=44,
  serialized_end=514,
)


_STARTTRACERESPONSE = _descriptor.Descriptor(
  name='StartTraceResponse',
  full_name='magma.orc8r.StartTraceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='magma.orc8r.StartTraceResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
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
  serialized_start=516,
  serialized_end=553,
)


_ENDTRACEREQUEST = _descriptor.Descriptor(
  name='EndTraceRequest',
  full_name='magma.orc8r.EndTraceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='trace_id', full_name='magma.orc8r.EndTraceRequest.trace_id', index=0,
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
  serialized_start=555,
  serialized_end=590,
)


_ENDTRACERESPONSE = _descriptor.Descriptor(
  name='EndTraceResponse',
  full_name='magma.orc8r.EndTraceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='magma.orc8r.EndTraceResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trace_content', full_name='magma.orc8r.EndTraceResponse.trace_content', index=1,
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
  serialized_start=592,
  serialized_end=650,
)


_REPORTENDEDTRACEREQUEST = _descriptor.Descriptor(
  name='ReportEndedTraceRequest',
  full_name='magma.orc8r.ReportEndedTraceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='trace_id', full_name='magma.orc8r.ReportEndedTraceRequest.trace_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='success', full_name='magma.orc8r.ReportEndedTraceRequest.success', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trace_content', full_name='magma.orc8r.ReportEndedTraceRequest.trace_content', index=2,
      number=3, type=12, cpp_type=9, label=1,
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
  serialized_start=652,
  serialized_end=735,
)


_REPORTENDEDTRACERESPONSE = _descriptor.Descriptor(
  name='ReportEndedTraceResponse',
  full_name='magma.orc8r.ReportEndedTraceResponse',
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
  serialized_start=737,
  serialized_end=763,
)

_STARTTRACEREQUEST.fields_by_name['trace_type'].enum_type = _STARTTRACEREQUEST_TRACETYPE
_STARTTRACEREQUEST.fields_by_name['protocol'].enum_type = _STARTTRACEREQUEST_PROTOCOLNAME
_STARTTRACEREQUEST.fields_by_name['interface'].enum_type = _STARTTRACEREQUEST_INTERFACENAME
_STARTTRACEREQUEST_TRACETYPE.containing_type = _STARTTRACEREQUEST
_STARTTRACEREQUEST_PROTOCOLNAME.containing_type = _STARTTRACEREQUEST
_STARTTRACEREQUEST_INTERFACENAME.containing_type = _STARTTRACEREQUEST
DESCRIPTOR.message_types_by_name['StartTraceRequest'] = _STARTTRACEREQUEST
DESCRIPTOR.message_types_by_name['StartTraceResponse'] = _STARTTRACERESPONSE
DESCRIPTOR.message_types_by_name['EndTraceRequest'] = _ENDTRACEREQUEST
DESCRIPTOR.message_types_by_name['EndTraceResponse'] = _ENDTRACERESPONSE
DESCRIPTOR.message_types_by_name['ReportEndedTraceRequest'] = _REPORTENDEDTRACEREQUEST
DESCRIPTOR.message_types_by_name['ReportEndedTraceResponse'] = _REPORTENDEDTRACERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StartTraceRequest = _reflection.GeneratedProtocolMessageType('StartTraceRequest', (_message.Message,), {
  'DESCRIPTOR' : _STARTTRACEREQUEST,
  '__module__' : 'orc8r.protos.ctraced_pb2'
  # @@protoc_insertion_point(class_scope:magma.orc8r.StartTraceRequest)
  })
_sym_db.RegisterMessage(StartTraceRequest)

StartTraceResponse = _reflection.GeneratedProtocolMessageType('StartTraceResponse', (_message.Message,), {
  'DESCRIPTOR' : _STARTTRACERESPONSE,
  '__module__' : 'orc8r.protos.ctraced_pb2'
  # @@protoc_insertion_point(class_scope:magma.orc8r.StartTraceResponse)
  })
_sym_db.RegisterMessage(StartTraceResponse)

EndTraceRequest = _reflection.GeneratedProtocolMessageType('EndTraceRequest', (_message.Message,), {
  'DESCRIPTOR' : _ENDTRACEREQUEST,
  '__module__' : 'orc8r.protos.ctraced_pb2'
  # @@protoc_insertion_point(class_scope:magma.orc8r.EndTraceRequest)
  })
_sym_db.RegisterMessage(EndTraceRequest)

EndTraceResponse = _reflection.GeneratedProtocolMessageType('EndTraceResponse', (_message.Message,), {
  'DESCRIPTOR' : _ENDTRACERESPONSE,
  '__module__' : 'orc8r.protos.ctraced_pb2'
  # @@protoc_insertion_point(class_scope:magma.orc8r.EndTraceResponse)
  })
_sym_db.RegisterMessage(EndTraceResponse)

ReportEndedTraceRequest = _reflection.GeneratedProtocolMessageType('ReportEndedTraceRequest', (_message.Message,), {
  'DESCRIPTOR' : _REPORTENDEDTRACEREQUEST,
  '__module__' : 'orc8r.protos.ctraced_pb2'
  # @@protoc_insertion_point(class_scope:magma.orc8r.ReportEndedTraceRequest)
  })
_sym_db.RegisterMessage(ReportEndedTraceRequest)

ReportEndedTraceResponse = _reflection.GeneratedProtocolMessageType('ReportEndedTraceResponse', (_message.Message,), {
  'DESCRIPTOR' : _REPORTENDEDTRACERESPONSE,
  '__module__' : 'orc8r.protos.ctraced_pb2'
  # @@protoc_insertion_point(class_scope:magma.orc8r.ReportEndedTraceResponse)
  })
_sym_db.RegisterMessage(ReportEndedTraceResponse)


DESCRIPTOR._options = None

_CALLTRACESERVICE = _descriptor.ServiceDescriptor(
  name='CallTraceService',
  full_name='magma.orc8r.CallTraceService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=766,
  serialized_end=948,
  methods=[
  _descriptor.MethodDescriptor(
    name='StartCallTrace',
    full_name='magma.orc8r.CallTraceService.StartCallTrace',
    index=0,
    containing_service=None,
    input_type=_STARTTRACEREQUEST,
    output_type=_STARTTRACERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='EndCallTrace',
    full_name='magma.orc8r.CallTraceService.EndCallTrace',
    index=1,
    containing_service=None,
    input_type=_ENDTRACEREQUEST,
    output_type=_ENDTRACERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CALLTRACESERVICE)

DESCRIPTOR.services_by_name['CallTraceService'] = _CALLTRACESERVICE


_CALLTRACECONTROLLER = _descriptor.ServiceDescriptor(
  name='CallTraceController',
  full_name='magma.orc8r.CallTraceController',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=950,
  serialized_end=1074,
  methods=[
  _descriptor.MethodDescriptor(
    name='ReportEndedCallTrace',
    full_name='magma.orc8r.CallTraceController.ReportEndedCallTrace',
    index=0,
    containing_service=None,
    input_type=_REPORTENDEDTRACEREQUEST,
    output_type=_REPORTENDEDTRACERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CALLTRACECONTROLLER)

DESCRIPTOR.services_by_name['CallTraceController'] = _CALLTRACECONTROLLER

# @@protoc_insertion_point(module_scope)
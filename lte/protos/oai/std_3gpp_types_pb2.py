# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lte/protos/oai/std_3gpp_types.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='lte/protos/oai/std_3gpp_types.proto',
  package='magma.lte.oai',
  syntax='proto3',
  serialized_options=b'Z\035magma/lte/cloud/go/protos/oai',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n#lte/protos/oai/std_3gpp_types.proto\x12\rmagma.lte.oai\"V\n\x0eParametersList\x12,\n\nparameters\x18\x01 \x03(\x0b\x32\x18.magma.lte.oai.Parameter\x12\x16\n\x0enum_parameters\x18\x02 \x01(\r\"K\n\tParameter\x12\x1c\n\x14parameter_identifier\x18\x01 \x01(\r\x12\x0e\n\x06length\x18\x02 \x01(\r\x12\x10\n\x08\x63ontents\x18\x03 \x01(\x0c\"\x99\x01\n\x03Pco\x12\x0b\n\x03\x65xt\x18\x01 \x01(\r\x12\r\n\x05spare\x18\x02 \x01(\r\x12\x1e\n\x16\x63onfiguration_protocol\x18\x03 \x01(\r\x12$\n\x1cnum_protocol_or_container_id\x18\x04 \x01(\r\x12\x30\n\x0cpco_protocol\x18\x05 \x03(\x0b\x32\x1a.magma.lte.oai.PcoProtocol\";\n\x0bPcoProtocol\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0e\n\x06length\x18\x02 \x01(\r\x12\x10\n\x08\x63ontents\x18\x03 \x01(\x0c\"Y\n\x05\x46teid\x12\x14\n\x0cipv4_address\x18\x01 \x01(\r\x12\x14\n\x0cipv6_address\x18\x02 \x01(\x0c\x12\x16\n\x0einterface_type\x18\x03 \x01(\r\x12\x0c\n\x04teid\x18\x04 \x01(\r\"2\n\tPortRange\x12\x11\n\tlow_limit\x18\x01 \x01(\r\x12\x12\n\nhigh_limit\x18\x02 \x01(\r\"8\n\x19TypeOfServiceTrafficClass\x12\r\n\x05value\x18\x01 \x01(\r\x12\x0c\n\x04mask\x18\x02 \x01(\r\"-\n\x0fIpRemoteAddress\x12\x0c\n\x04\x61\x64\x64r\x18\x01 \x01(\r\x12\x0c\n\x04mask\x18\x02 \x01(\r\"\xf2\x03\n\x14PacketFilterContents\x12\r\n\x05\x66lags\x18\x01 \x01(\r\x12=\n\x15ipv4_remote_addresses\x18\x02 \x03(\x0b\x32\x1e.magma.lte.oai.IpRemoteAddress\x12=\n\x15ipv6_remote_addresses\x18\x03 \x03(\x0b\x32\x1e.magma.lte.oai.IpRemoteAddress\x12&\n\x1eprotocol_identifier_nextheader\x18\x04 \x01(\r\x12\x19\n\x11single_local_port\x18\n \x01(\r\x12\x32\n\x10local_port_range\x18\x0b \x01(\x0b\x32\x18.magma.lte.oai.PortRange\x12\x1a\n\x12single_remote_port\x18\x0c \x01(\r\x12\x33\n\x11remote_port_range\x18\r \x01(\x0b\x32\x18.magma.lte.oai.PortRange\x12 \n\x18security_parameter_index\x18\x14 \x01(\r\x12O\n\x1dtype_of_service_traffic_class\x18\x15 \x01(\x0b\x32(.magma.lte.oai.TypeOfServiceTrafficClass\x12\x12\n\nflow_label\x18\x16 \x01(\rB\x1fZ\x1dmagma/lte/cloud/go/protos/oaib\x06proto3'
)




_PARAMETERSLIST = _descriptor.Descriptor(
  name='ParametersList',
  full_name='magma.lte.oai.ParametersList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parameters', full_name='magma.lte.oai.ParametersList.parameters', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_parameters', full_name='magma.lte.oai.ParametersList.num_parameters', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=54,
  serialized_end=140,
)


_PARAMETER = _descriptor.Descriptor(
  name='Parameter',
  full_name='magma.lte.oai.Parameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parameter_identifier', full_name='magma.lte.oai.Parameter.parameter_identifier', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='length', full_name='magma.lte.oai.Parameter.length', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contents', full_name='magma.lte.oai.Parameter.contents', index=2,
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
  serialized_start=142,
  serialized_end=217,
)


_PCO = _descriptor.Descriptor(
  name='Pco',
  full_name='magma.lte.oai.Pco',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='magma.lte.oai.Pco.ext', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='spare', full_name='magma.lte.oai.Pco.spare', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='configuration_protocol', full_name='magma.lte.oai.Pco.configuration_protocol', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_protocol_or_container_id', full_name='magma.lte.oai.Pco.num_protocol_or_container_id', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pco_protocol', full_name='magma.lte.oai.Pco.pco_protocol', index=4,
      number=5, type=11, cpp_type=10, label=3,
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
  serialized_start=220,
  serialized_end=373,
)


_PCOPROTOCOL = _descriptor.Descriptor(
  name='PcoProtocol',
  full_name='magma.lte.oai.PcoProtocol',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='magma.lte.oai.PcoProtocol.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='length', full_name='magma.lte.oai.PcoProtocol.length', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contents', full_name='magma.lte.oai.PcoProtocol.contents', index=2,
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
  serialized_start=375,
  serialized_end=434,
)


_FTEID = _descriptor.Descriptor(
  name='Fteid',
  full_name='magma.lte.oai.Fteid',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ipv4_address', full_name='magma.lte.oai.Fteid.ipv4_address', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ipv6_address', full_name='magma.lte.oai.Fteid.ipv6_address', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='interface_type', full_name='magma.lte.oai.Fteid.interface_type', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='teid', full_name='magma.lte.oai.Fteid.teid', index=3,
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
  serialized_start=436,
  serialized_end=525,
)


_PORTRANGE = _descriptor.Descriptor(
  name='PortRange',
  full_name='magma.lte.oai.PortRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='low_limit', full_name='magma.lte.oai.PortRange.low_limit', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='high_limit', full_name='magma.lte.oai.PortRange.high_limit', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=527,
  serialized_end=577,
)


_TYPEOFSERVICETRAFFICCLASS = _descriptor.Descriptor(
  name='TypeOfServiceTrafficClass',
  full_name='magma.lte.oai.TypeOfServiceTrafficClass',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='magma.lte.oai.TypeOfServiceTrafficClass.value', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mask', full_name='magma.lte.oai.TypeOfServiceTrafficClass.mask', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=579,
  serialized_end=635,
)


_IPREMOTEADDRESS = _descriptor.Descriptor(
  name='IpRemoteAddress',
  full_name='magma.lte.oai.IpRemoteAddress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='addr', full_name='magma.lte.oai.IpRemoteAddress.addr', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mask', full_name='magma.lte.oai.IpRemoteAddress.mask', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=637,
  serialized_end=682,
)


_PACKETFILTERCONTENTS = _descriptor.Descriptor(
  name='PacketFilterContents',
  full_name='magma.lte.oai.PacketFilterContents',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='flags', full_name='magma.lte.oai.PacketFilterContents.flags', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ipv4_remote_addresses', full_name='magma.lte.oai.PacketFilterContents.ipv4_remote_addresses', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ipv6_remote_addresses', full_name='magma.lte.oai.PacketFilterContents.ipv6_remote_addresses', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='protocol_identifier_nextheader', full_name='magma.lte.oai.PacketFilterContents.protocol_identifier_nextheader', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='single_local_port', full_name='magma.lte.oai.PacketFilterContents.single_local_port', index=4,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='local_port_range', full_name='magma.lte.oai.PacketFilterContents.local_port_range', index=5,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='single_remote_port', full_name='magma.lte.oai.PacketFilterContents.single_remote_port', index=6,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='remote_port_range', full_name='magma.lte.oai.PacketFilterContents.remote_port_range', index=7,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='security_parameter_index', full_name='magma.lte.oai.PacketFilterContents.security_parameter_index', index=8,
      number=20, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type_of_service_traffic_class', full_name='magma.lte.oai.PacketFilterContents.type_of_service_traffic_class', index=9,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='flow_label', full_name='magma.lte.oai.PacketFilterContents.flow_label', index=10,
      number=22, type=13, cpp_type=3, label=1,
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
  serialized_start=685,
  serialized_end=1183,
)

_PARAMETERSLIST.fields_by_name['parameters'].message_type = _PARAMETER
_PCO.fields_by_name['pco_protocol'].message_type = _PCOPROTOCOL
_PACKETFILTERCONTENTS.fields_by_name['ipv4_remote_addresses'].message_type = _IPREMOTEADDRESS
_PACKETFILTERCONTENTS.fields_by_name['ipv6_remote_addresses'].message_type = _IPREMOTEADDRESS
_PACKETFILTERCONTENTS.fields_by_name['local_port_range'].message_type = _PORTRANGE
_PACKETFILTERCONTENTS.fields_by_name['remote_port_range'].message_type = _PORTRANGE
_PACKETFILTERCONTENTS.fields_by_name['type_of_service_traffic_class'].message_type = _TYPEOFSERVICETRAFFICCLASS
DESCRIPTOR.message_types_by_name['ParametersList'] = _PARAMETERSLIST
DESCRIPTOR.message_types_by_name['Parameter'] = _PARAMETER
DESCRIPTOR.message_types_by_name['Pco'] = _PCO
DESCRIPTOR.message_types_by_name['PcoProtocol'] = _PCOPROTOCOL
DESCRIPTOR.message_types_by_name['Fteid'] = _FTEID
DESCRIPTOR.message_types_by_name['PortRange'] = _PORTRANGE
DESCRIPTOR.message_types_by_name['TypeOfServiceTrafficClass'] = _TYPEOFSERVICETRAFFICCLASS
DESCRIPTOR.message_types_by_name['IpRemoteAddress'] = _IPREMOTEADDRESS
DESCRIPTOR.message_types_by_name['PacketFilterContents'] = _PACKETFILTERCONTENTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ParametersList = _reflection.GeneratedProtocolMessageType('ParametersList', (_message.Message,), {
  'DESCRIPTOR' : _PARAMETERSLIST,
  '__module__' : 'lte.protos.oai.std_3gpp_types_pb2'
  # @@protoc_insertion_point(class_scope:magma.lte.oai.ParametersList)
  })
_sym_db.RegisterMessage(ParametersList)

Parameter = _reflection.GeneratedProtocolMessageType('Parameter', (_message.Message,), {
  'DESCRIPTOR' : _PARAMETER,
  '__module__' : 'lte.protos.oai.std_3gpp_types_pb2'
  # @@protoc_insertion_point(class_scope:magma.lte.oai.Parameter)
  })
_sym_db.RegisterMessage(Parameter)

Pco = _reflection.GeneratedProtocolMessageType('Pco', (_message.Message,), {
  'DESCRIPTOR' : _PCO,
  '__module__' : 'lte.protos.oai.std_3gpp_types_pb2'
  # @@protoc_insertion_point(class_scope:magma.lte.oai.Pco)
  })
_sym_db.RegisterMessage(Pco)

PcoProtocol = _reflection.GeneratedProtocolMessageType('PcoProtocol', (_message.Message,), {
  'DESCRIPTOR' : _PCOPROTOCOL,
  '__module__' : 'lte.protos.oai.std_3gpp_types_pb2'
  # @@protoc_insertion_point(class_scope:magma.lte.oai.PcoProtocol)
  })
_sym_db.RegisterMessage(PcoProtocol)

Fteid = _reflection.GeneratedProtocolMessageType('Fteid', (_message.Message,), {
  'DESCRIPTOR' : _FTEID,
  '__module__' : 'lte.protos.oai.std_3gpp_types_pb2'
  # @@protoc_insertion_point(class_scope:magma.lte.oai.Fteid)
  })
_sym_db.RegisterMessage(Fteid)

PortRange = _reflection.GeneratedProtocolMessageType('PortRange', (_message.Message,), {
  'DESCRIPTOR' : _PORTRANGE,
  '__module__' : 'lte.protos.oai.std_3gpp_types_pb2'
  # @@protoc_insertion_point(class_scope:magma.lte.oai.PortRange)
  })
_sym_db.RegisterMessage(PortRange)

TypeOfServiceTrafficClass = _reflection.GeneratedProtocolMessageType('TypeOfServiceTrafficClass', (_message.Message,), {
  'DESCRIPTOR' : _TYPEOFSERVICETRAFFICCLASS,
  '__module__' : 'lte.protos.oai.std_3gpp_types_pb2'
  # @@protoc_insertion_point(class_scope:magma.lte.oai.TypeOfServiceTrafficClass)
  })
_sym_db.RegisterMessage(TypeOfServiceTrafficClass)

IpRemoteAddress = _reflection.GeneratedProtocolMessageType('IpRemoteAddress', (_message.Message,), {
  'DESCRIPTOR' : _IPREMOTEADDRESS,
  '__module__' : 'lte.protos.oai.std_3gpp_types_pb2'
  # @@protoc_insertion_point(class_scope:magma.lte.oai.IpRemoteAddress)
  })
_sym_db.RegisterMessage(IpRemoteAddress)

PacketFilterContents = _reflection.GeneratedProtocolMessageType('PacketFilterContents', (_message.Message,), {
  'DESCRIPTOR' : _PACKETFILTERCONTENTS,
  '__module__' : 'lte.protos.oai.std_3gpp_types_pb2'
  # @@protoc_insertion_point(class_scope:magma.lte.oai.PacketFilterContents)
  })
_sym_db.RegisterMessage(PacketFilterContents)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
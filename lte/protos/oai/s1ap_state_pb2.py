# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lte/protos/oai/s1ap_state.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='lte/protos/oai/s1ap_state.proto',
  package='magma.lte.oai',
  syntax='proto3',
  serialized_options=b'Z\035magma/lte/cloud/go/protos/oai',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1flte/protos/oai/s1ap_state.proto\x12\rmagma.lte.oai\"$\n\tS1apTimer\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0b\n\x03sec\x18\x02 \x01(\x05\"I\n\x11SupportedTaiItems\x12\x0b\n\x03tac\x18\x01 \x01(\r\x12\x17\n\x0f\x62plmnlist_count\x18\x02 \x01(\r\x12\x0e\n\x06\x62plmns\x18\x03 \x03(\x0c\"d\n\x0fSupportedTaList\x12\x12\n\nlist_count\x18\x01 \x01(\r\x12=\n\x13supported_tai_items\x18\x02 \x03(\x0b\x32 .magma.lte.oai.SupportedTaiItems\"\xa6\x03\n\x0e\x45nbDescription\x12\x0e\n\x06\x65nb_id\x18\x01 \x01(\r\x12\x10\n\x08s1_state\x18\x02 \x01(\x05\x12\x10\n\x08\x65nb_name\x18\x03 \x01(\x0c\x12\x1a\n\x12\x64\x65\x66\x61ult_paging_drx\x18\x04 \x01(\r\x12\x18\n\x10nb_ue_associated\x18\x05 \x01(\r\x12\x15\n\rsctp_assoc_id\x18\x06 \x01(\r\x12\x18\n\x10next_sctp_stream\x18\x07 \x01(\r\x12\x11\n\tinstreams\x18\x08 \x01(\r\x12\x12\n\noutstreams\x18\t \x01(\r\x12\x38\n\x06ue_ids\x18\n \x03(\x0b\x32(.magma.lte.oai.EnbDescription.UeIdsEntry\x12\x39\n\x11supported_ta_list\x18\x0b \x01(\x0b\x32\x1e.magma.lte.oai.SupportedTaList\x12\x15\n\rran_cp_ipaddr\x18\x0c \x01(\x0c\x12\x18\n\x10ran_cp_ipaddr_sz\x18\r \x01(\r\x1a,\n\nUeIdsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12\r\n\x05value\x18\x02 \x01(\x04:\x02\x38\x01\"\x9b\x02\n\rUeDescription\x12\x13\n\x0bs1_ue_state\x18\x02 \x01(\x05\x12\x16\n\x0e\x65nb_ue_s1ap_id\x18\x03 \x01(\r\x12\x16\n\x0emme_ue_s1ap_id\x18\x04 \x01(\r\x12\x18\n\x10sctp_stream_recv\x18\x05 \x01(\r\x12\x18\n\x10sctp_stream_send\x18\x06 \x01(\r\x12;\n\x19s1ap_ue_context_rel_timer\x18\x07 \x01(\x0b\x32\x18.magma.lte.oai.S1apTimer\x12\x15\n\rsctp_assoc_id\x18\x08 \x01(\r\x12=\n\x13s1ap_handover_state\x18\t \x01(\x0b\x32 .magma.lte.oai.S1apHandoverState\"\x95\x02\n\tS1apState\x12\x30\n\x04\x65nbs\x18\x01 \x03(\x0b\x32\".magma.lte.oai.S1apState.EnbsEntry\x12\x42\n\rmmeid2associd\x18\x02 \x03(\x0b\x32+.magma.lte.oai.S1apState.Mmeid2associdEntry\x12\x10\n\x08num_enbs\x18\x03 \x01(\r\x1aJ\n\tEnbsEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x1d.magma.lte.oai.EnbDescription:\x02\x38\x01\x1a\x34\n\x12Mmeid2associdEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\"\x90\x01\n\x0bS1apImsiMap\x12J\n\x12mme_ue_id_imsi_map\x18\x01 \x03(\x0b\x32..magma.lte.oai.S1apImsiMap.MmeUeIdImsiMapEntry\x1a\x35\n\x13MmeUeIdImsiMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12\r\n\x05value\x18\x02 \x01(\x04:\x02\x38\x01\"\xba\x01\n\x11S1apHandoverState\x12\x16\n\x0emme_ue_s1ap_id\x18\x01 \x01(\r\x12\x15\n\rsource_enb_id\x18\x02 \x01(\r\x12\x15\n\rtarget_enb_id\x18\x03 \x01(\r\x12\x1d\n\x15target_enb_ue_s1ap_id\x18\x04 \x01(\r\x12\x1f\n\x17target_sctp_stream_recv\x18\x05 \x01(\r\x12\x1f\n\x17target_sctp_stream_send\x18\x06 \x01(\rB\x1fZ\x1dmagma/lte/cloud/go/protos/oaib\x06proto3'
)




_S1APTIMER = _descriptor.Descriptor(
  name='S1apTimer',
  full_name='magma.lte.oai.S1apTimer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='magma.lte.oai.S1apTimer.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sec', full_name='magma.lte.oai.S1apTimer.sec', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=50,
  serialized_end=86,
)


_SUPPORTEDTAIITEMS = _descriptor.Descriptor(
  name='SupportedTaiItems',
  full_name='magma.lte.oai.SupportedTaiItems',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tac', full_name='magma.lte.oai.SupportedTaiItems.tac', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bplmnlist_count', full_name='magma.lte.oai.SupportedTaiItems.bplmnlist_count', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bplmns', full_name='magma.lte.oai.SupportedTaiItems.bplmns', index=2,
      number=3, type=12, cpp_type=9, label=3,
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
  serialized_start=88,
  serialized_end=161,
)


_SUPPORTEDTALIST = _descriptor.Descriptor(
  name='SupportedTaList',
  full_name='magma.lte.oai.SupportedTaList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='list_count', full_name='magma.lte.oai.SupportedTaList.list_count', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='supported_tai_items', full_name='magma.lte.oai.SupportedTaList.supported_tai_items', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=163,
  serialized_end=263,
)


_ENBDESCRIPTION_UEIDSENTRY = _descriptor.Descriptor(
  name='UeIdsEntry',
  full_name='magma.lte.oai.EnbDescription.UeIdsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='magma.lte.oai.EnbDescription.UeIdsEntry.key', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='magma.lte.oai.EnbDescription.UeIdsEntry.value', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=644,
  serialized_end=688,
)

_ENBDESCRIPTION = _descriptor.Descriptor(
  name='EnbDescription',
  full_name='magma.lte.oai.EnbDescription',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='enb_id', full_name='magma.lte.oai.EnbDescription.enb_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='s1_state', full_name='magma.lte.oai.EnbDescription.s1_state', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enb_name', full_name='magma.lte.oai.EnbDescription.enb_name', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='default_paging_drx', full_name='magma.lte.oai.EnbDescription.default_paging_drx', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nb_ue_associated', full_name='magma.lte.oai.EnbDescription.nb_ue_associated', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sctp_assoc_id', full_name='magma.lte.oai.EnbDescription.sctp_assoc_id', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_sctp_stream', full_name='magma.lte.oai.EnbDescription.next_sctp_stream', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='instreams', full_name='magma.lte.oai.EnbDescription.instreams', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='outstreams', full_name='magma.lte.oai.EnbDescription.outstreams', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ue_ids', full_name='magma.lte.oai.EnbDescription.ue_ids', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='supported_ta_list', full_name='magma.lte.oai.EnbDescription.supported_ta_list', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ran_cp_ipaddr', full_name='magma.lte.oai.EnbDescription.ran_cp_ipaddr', index=11,
      number=12, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ran_cp_ipaddr_sz', full_name='magma.lte.oai.EnbDescription.ran_cp_ipaddr_sz', index=12,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ENBDESCRIPTION_UEIDSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=266,
  serialized_end=688,
)


_UEDESCRIPTION = _descriptor.Descriptor(
  name='UeDescription',
  full_name='magma.lte.oai.UeDescription',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='s1_ue_state', full_name='magma.lte.oai.UeDescription.s1_ue_state', index=0,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enb_ue_s1ap_id', full_name='magma.lte.oai.UeDescription.enb_ue_s1ap_id', index=1,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mme_ue_s1ap_id', full_name='magma.lte.oai.UeDescription.mme_ue_s1ap_id', index=2,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sctp_stream_recv', full_name='magma.lte.oai.UeDescription.sctp_stream_recv', index=3,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sctp_stream_send', full_name='magma.lte.oai.UeDescription.sctp_stream_send', index=4,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='s1ap_ue_context_rel_timer', full_name='magma.lte.oai.UeDescription.s1ap_ue_context_rel_timer', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sctp_assoc_id', full_name='magma.lte.oai.UeDescription.sctp_assoc_id', index=6,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='s1ap_handover_state', full_name='magma.lte.oai.UeDescription.s1ap_handover_state', index=7,
      number=9, type=11, cpp_type=10, label=1,
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
  serialized_start=691,
  serialized_end=974,
)


_S1APSTATE_ENBSENTRY = _descriptor.Descriptor(
  name='EnbsEntry',
  full_name='magma.lte.oai.S1apState.EnbsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='magma.lte.oai.S1apState.EnbsEntry.key', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='magma.lte.oai.S1apState.EnbsEntry.value', index=1,
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
  serialized_start=1126,
  serialized_end=1200,
)

_S1APSTATE_MMEID2ASSOCIDENTRY = _descriptor.Descriptor(
  name='Mmeid2associdEntry',
  full_name='magma.lte.oai.S1apState.Mmeid2associdEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='magma.lte.oai.S1apState.Mmeid2associdEntry.key', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='magma.lte.oai.S1apState.Mmeid2associdEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1202,
  serialized_end=1254,
)

_S1APSTATE = _descriptor.Descriptor(
  name='S1apState',
  full_name='magma.lte.oai.S1apState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='enbs', full_name='magma.lte.oai.S1apState.enbs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mmeid2associd', full_name='magma.lte.oai.S1apState.mmeid2associd', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_enbs', full_name='magma.lte.oai.S1apState.num_enbs', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_S1APSTATE_ENBSENTRY, _S1APSTATE_MMEID2ASSOCIDENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=977,
  serialized_end=1254,
)


_S1APIMSIMAP_MMEUEIDIMSIMAPENTRY = _descriptor.Descriptor(
  name='MmeUeIdImsiMapEntry',
  full_name='magma.lte.oai.S1apImsiMap.MmeUeIdImsiMapEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='magma.lte.oai.S1apImsiMap.MmeUeIdImsiMapEntry.key', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='magma.lte.oai.S1apImsiMap.MmeUeIdImsiMapEntry.value', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1348,
  serialized_end=1401,
)

_S1APIMSIMAP = _descriptor.Descriptor(
  name='S1apImsiMap',
  full_name='magma.lte.oai.S1apImsiMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mme_ue_id_imsi_map', full_name='magma.lte.oai.S1apImsiMap.mme_ue_id_imsi_map', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_S1APIMSIMAP_MMEUEIDIMSIMAPENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1257,
  serialized_end=1401,
)


_S1APHANDOVERSTATE = _descriptor.Descriptor(
  name='S1apHandoverState',
  full_name='magma.lte.oai.S1apHandoverState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mme_ue_s1ap_id', full_name='magma.lte.oai.S1apHandoverState.mme_ue_s1ap_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source_enb_id', full_name='magma.lte.oai.S1apHandoverState.source_enb_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_enb_id', full_name='magma.lte.oai.S1apHandoverState.target_enb_id', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_enb_ue_s1ap_id', full_name='magma.lte.oai.S1apHandoverState.target_enb_ue_s1ap_id', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_sctp_stream_recv', full_name='magma.lte.oai.S1apHandoverState.target_sctp_stream_recv', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_sctp_stream_send', full_name='magma.lte.oai.S1apHandoverState.target_sctp_stream_send', index=5,
      number=6, type=13, cpp_type=3, label=1,
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
  serialized_start=1404,
  serialized_end=1590,
)

_SUPPORTEDTALIST.fields_by_name['supported_tai_items'].message_type = _SUPPORTEDTAIITEMS
_ENBDESCRIPTION_UEIDSENTRY.containing_type = _ENBDESCRIPTION
_ENBDESCRIPTION.fields_by_name['ue_ids'].message_type = _ENBDESCRIPTION_UEIDSENTRY
_ENBDESCRIPTION.fields_by_name['supported_ta_list'].message_type = _SUPPORTEDTALIST
_UEDESCRIPTION.fields_by_name['s1ap_ue_context_rel_timer'].message_type = _S1APTIMER
_UEDESCRIPTION.fields_by_name['s1ap_handover_state'].message_type = _S1APHANDOVERSTATE
_S1APSTATE_ENBSENTRY.fields_by_name['value'].message_type = _ENBDESCRIPTION
_S1APSTATE_ENBSENTRY.containing_type = _S1APSTATE
_S1APSTATE_MMEID2ASSOCIDENTRY.containing_type = _S1APSTATE
_S1APSTATE.fields_by_name['enbs'].message_type = _S1APSTATE_ENBSENTRY
_S1APSTATE.fields_by_name['mmeid2associd'].message_type = _S1APSTATE_MMEID2ASSOCIDENTRY
_S1APIMSIMAP_MMEUEIDIMSIMAPENTRY.containing_type = _S1APIMSIMAP
_S1APIMSIMAP.fields_by_name['mme_ue_id_imsi_map'].message_type = _S1APIMSIMAP_MMEUEIDIMSIMAPENTRY
DESCRIPTOR.message_types_by_name['S1apTimer'] = _S1APTIMER
DESCRIPTOR.message_types_by_name['SupportedTaiItems'] = _SUPPORTEDTAIITEMS
DESCRIPTOR.message_types_by_name['SupportedTaList'] = _SUPPORTEDTALIST
DESCRIPTOR.message_types_by_name['EnbDescription'] = _ENBDESCRIPTION
DESCRIPTOR.message_types_by_name['UeDescription'] = _UEDESCRIPTION
DESCRIPTOR.message_types_by_name['S1apState'] = _S1APSTATE
DESCRIPTOR.message_types_by_name['S1apImsiMap'] = _S1APIMSIMAP
DESCRIPTOR.message_types_by_name['S1apHandoverState'] = _S1APHANDOVERSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

S1apTimer = _reflection.GeneratedProtocolMessageType('S1apTimer', (_message.Message,), {
  'DESCRIPTOR' : _S1APTIMER,
  '__module__' : 'lte.protos.oai.s1ap_state_pb2'
  # @@protoc_insertion_point(class_scope:magma.lte.oai.S1apTimer)
  })
_sym_db.RegisterMessage(S1apTimer)

SupportedTaiItems = _reflection.GeneratedProtocolMessageType('SupportedTaiItems', (_message.Message,), {
  'DESCRIPTOR' : _SUPPORTEDTAIITEMS,
  '__module__' : 'lte.protos.oai.s1ap_state_pb2'
  # @@protoc_insertion_point(class_scope:magma.lte.oai.SupportedTaiItems)
  })
_sym_db.RegisterMessage(SupportedTaiItems)

SupportedTaList = _reflection.GeneratedProtocolMessageType('SupportedTaList', (_message.Message,), {
  'DESCRIPTOR' : _SUPPORTEDTALIST,
  '__module__' : 'lte.protos.oai.s1ap_state_pb2'
  # @@protoc_insertion_point(class_scope:magma.lte.oai.SupportedTaList)
  })
_sym_db.RegisterMessage(SupportedTaList)

EnbDescription = _reflection.GeneratedProtocolMessageType('EnbDescription', (_message.Message,), {

  'UeIdsEntry' : _reflection.GeneratedProtocolMessageType('UeIdsEntry', (_message.Message,), {
    'DESCRIPTOR' : _ENBDESCRIPTION_UEIDSENTRY,
    '__module__' : 'lte.protos.oai.s1ap_state_pb2'
    # @@protoc_insertion_point(class_scope:magma.lte.oai.EnbDescription.UeIdsEntry)
    })
  ,
  'DESCRIPTOR' : _ENBDESCRIPTION,
  '__module__' : 'lte.protos.oai.s1ap_state_pb2'
  # @@protoc_insertion_point(class_scope:magma.lte.oai.EnbDescription)
  })
_sym_db.RegisterMessage(EnbDescription)
_sym_db.RegisterMessage(EnbDescription.UeIdsEntry)

UeDescription = _reflection.GeneratedProtocolMessageType('UeDescription', (_message.Message,), {
  'DESCRIPTOR' : _UEDESCRIPTION,
  '__module__' : 'lte.protos.oai.s1ap_state_pb2'
  # @@protoc_insertion_point(class_scope:magma.lte.oai.UeDescription)
  })
_sym_db.RegisterMessage(UeDescription)

S1apState = _reflection.GeneratedProtocolMessageType('S1apState', (_message.Message,), {

  'EnbsEntry' : _reflection.GeneratedProtocolMessageType('EnbsEntry', (_message.Message,), {
    'DESCRIPTOR' : _S1APSTATE_ENBSENTRY,
    '__module__' : 'lte.protos.oai.s1ap_state_pb2'
    # @@protoc_insertion_point(class_scope:magma.lte.oai.S1apState.EnbsEntry)
    })
  ,

  'Mmeid2associdEntry' : _reflection.GeneratedProtocolMessageType('Mmeid2associdEntry', (_message.Message,), {
    'DESCRIPTOR' : _S1APSTATE_MMEID2ASSOCIDENTRY,
    '__module__' : 'lte.protos.oai.s1ap_state_pb2'
    # @@protoc_insertion_point(class_scope:magma.lte.oai.S1apState.Mmeid2associdEntry)
    })
  ,
  'DESCRIPTOR' : _S1APSTATE,
  '__module__' : 'lte.protos.oai.s1ap_state_pb2'
  # @@protoc_insertion_point(class_scope:magma.lte.oai.S1apState)
  })
_sym_db.RegisterMessage(S1apState)
_sym_db.RegisterMessage(S1apState.EnbsEntry)
_sym_db.RegisterMessage(S1apState.Mmeid2associdEntry)

S1apImsiMap = _reflection.GeneratedProtocolMessageType('S1apImsiMap', (_message.Message,), {

  'MmeUeIdImsiMapEntry' : _reflection.GeneratedProtocolMessageType('MmeUeIdImsiMapEntry', (_message.Message,), {
    'DESCRIPTOR' : _S1APIMSIMAP_MMEUEIDIMSIMAPENTRY,
    '__module__' : 'lte.protos.oai.s1ap_state_pb2'
    # @@protoc_insertion_point(class_scope:magma.lte.oai.S1apImsiMap.MmeUeIdImsiMapEntry)
    })
  ,
  'DESCRIPTOR' : _S1APIMSIMAP,
  '__module__' : 'lte.protos.oai.s1ap_state_pb2'
  # @@protoc_insertion_point(class_scope:magma.lte.oai.S1apImsiMap)
  })
_sym_db.RegisterMessage(S1apImsiMap)
_sym_db.RegisterMessage(S1apImsiMap.MmeUeIdImsiMapEntry)

S1apHandoverState = _reflection.GeneratedProtocolMessageType('S1apHandoverState', (_message.Message,), {
  'DESCRIPTOR' : _S1APHANDOVERSTATE,
  '__module__' : 'lte.protos.oai.s1ap_state_pb2'
  # @@protoc_insertion_point(class_scope:magma.lte.oai.S1apHandoverState)
  })
_sym_db.RegisterMessage(S1apHandoverState)


DESCRIPTOR._options = None
_ENBDESCRIPTION_UEIDSENTRY._options = None
_S1APSTATE_ENBSENTRY._options = None
_S1APSTATE_MMEID2ASSOCIDENTRY._options = None
_S1APIMSIMAP_MMEUEIDIMSIMAPENTRY._options = None
# @@protoc_insertion_point(module_scope)

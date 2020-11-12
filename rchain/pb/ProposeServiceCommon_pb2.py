# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ProposeServiceCommon.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from .scalapb import scalapb_pb2 as scalapb_dot_scalapb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ProposeServiceCommon.proto',
  package='casper',
  syntax='proto3',
  serialized_options=b'\342?!\n\033coop.rchain.casper.protocol\020\001(\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1aProposeServiceCommon.proto\x12\x06\x63\x61sper\x1a\x15scalapb/scalapb.proto\"7\n\x18PrintUnmatchedSendsQuery\x12\x1b\n\x13printUnmatchedSends\x18\x01 \x01(\x08\"\x14\n\x12ProposeResultQueryB$\xe2?!\n\x1b\x63oop.rchain.casper.protocol\x10\x01(\x01\x62\x06proto3'
  ,
  dependencies=[scalapb_dot_scalapb__pb2.DESCRIPTOR,])




_PRINTUNMATCHEDSENDSQUERY = _descriptor.Descriptor(
  name='PrintUnmatchedSendsQuery',
  full_name='casper.PrintUnmatchedSendsQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='printUnmatchedSends', full_name='casper.PrintUnmatchedSendsQuery.printUnmatchedSends', index=0,
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
  serialized_start=61,
  serialized_end=116,
)


_PROPOSERESULTQUERY = _descriptor.Descriptor(
  name='ProposeResultQuery',
  full_name='casper.ProposeResultQuery',
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
  serialized_start=118,
  serialized_end=138,
)

DESCRIPTOR.message_types_by_name['PrintUnmatchedSendsQuery'] = _PRINTUNMATCHEDSENDSQUERY
DESCRIPTOR.message_types_by_name['ProposeResultQuery'] = _PROPOSERESULTQUERY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PrintUnmatchedSendsQuery = _reflection.GeneratedProtocolMessageType('PrintUnmatchedSendsQuery', (_message.Message,), {
  'DESCRIPTOR' : _PRINTUNMATCHEDSENDSQUERY,
  '__module__' : 'ProposeServiceCommon_pb2'
  # @@protoc_insertion_point(class_scope:casper.PrintUnmatchedSendsQuery)
  })
_sym_db.RegisterMessage(PrintUnmatchedSendsQuery)

ProposeResultQuery = _reflection.GeneratedProtocolMessageType('ProposeResultQuery', (_message.Message,), {
  'DESCRIPTOR' : _PROPOSERESULTQUERY,
  '__module__' : 'ProposeServiceCommon_pb2'
  # @@protoc_insertion_point(class_scope:casper.ProposeResultQuery)
  })
_sym_db.RegisterMessage(ProposeResultQuery)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)

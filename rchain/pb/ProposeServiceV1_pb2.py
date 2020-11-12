# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ProposeServiceV1.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import ServiceError_pb2 as ServiceError__pb2
from . import ProposeServiceCommon_pb2 as ProposeServiceCommon__pb2
from .scalapb import scalapb_pb2 as scalapb_dot_scalapb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ProposeServiceV1.proto',
  package='casper.v1',
  syntax='proto3',
  serialized_options=b'\342?,\n&coop.rchain.casper.protocol.propose.v1\020\001(\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16ProposeServiceV1.proto\x12\tcasper.v1\x1a\x12ServiceError.proto\x1a\x1aProposeServiceCommon.proto\x1a\x15scalapb/scalapb.proto\"N\n\x0fProposeResponse\x12\x1e\n\x05\x65rror\x18\x01 \x01(\x0b\x32\r.ServiceErrorH\x00\x12\x10\n\x06result\x18\x02 \x01(\tH\x00\x42\t\n\x07message\"T\n\x15ProposeResultResponse\x12\x1e\n\x05\x65rror\x18\x01 \x01(\x0b\x32\r.ServiceErrorH\x00\x12\x10\n\x06result\x18\x02 \x01(\tH\x00\x42\t\n\x07message2\xac\x01\n\x0eProposeService\x12I\n\x07propose\x12 .casper.PrintUnmatchedSendsQuery\x1a\x1a.casper.v1.ProposeResponse\"\x00\x12O\n\rproposeResult\x12\x1a.casper.ProposeResultQuery\x1a .casper.v1.ProposeResultResponse\"\x00\x42/\xe2?,\n&coop.rchain.casper.protocol.propose.v1\x10\x01(\x01\x62\x06proto3'
  ,
  dependencies=[ServiceError__pb2.DESCRIPTOR,ProposeServiceCommon__pb2.DESCRIPTOR,scalapb_dot_scalapb__pb2.DESCRIPTOR,])




_PROPOSERESPONSE = _descriptor.Descriptor(
  name='ProposeResponse',
  full_name='casper.v1.ProposeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='casper.v1.ProposeResponse.error', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result', full_name='casper.v1.ProposeResponse.result', index=1,
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
    _descriptor.OneofDescriptor(
      name='message', full_name='casper.v1.ProposeResponse.message',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=108,
  serialized_end=186,
)


_PROPOSERESULTRESPONSE = _descriptor.Descriptor(
  name='ProposeResultResponse',
  full_name='casper.v1.ProposeResultResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='casper.v1.ProposeResultResponse.error', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result', full_name='casper.v1.ProposeResultResponse.result', index=1,
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
    _descriptor.OneofDescriptor(
      name='message', full_name='casper.v1.ProposeResultResponse.message',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=188,
  serialized_end=272,
)

_PROPOSERESPONSE.fields_by_name['error'].message_type = ServiceError__pb2._SERVICEERROR
_PROPOSERESPONSE.oneofs_by_name['message'].fields.append(
  _PROPOSERESPONSE.fields_by_name['error'])
_PROPOSERESPONSE.fields_by_name['error'].containing_oneof = _PROPOSERESPONSE.oneofs_by_name['message']
_PROPOSERESPONSE.oneofs_by_name['message'].fields.append(
  _PROPOSERESPONSE.fields_by_name['result'])
_PROPOSERESPONSE.fields_by_name['result'].containing_oneof = _PROPOSERESPONSE.oneofs_by_name['message']
_PROPOSERESULTRESPONSE.fields_by_name['error'].message_type = ServiceError__pb2._SERVICEERROR
_PROPOSERESULTRESPONSE.oneofs_by_name['message'].fields.append(
  _PROPOSERESULTRESPONSE.fields_by_name['error'])
_PROPOSERESULTRESPONSE.fields_by_name['error'].containing_oneof = _PROPOSERESULTRESPONSE.oneofs_by_name['message']
_PROPOSERESULTRESPONSE.oneofs_by_name['message'].fields.append(
  _PROPOSERESULTRESPONSE.fields_by_name['result'])
_PROPOSERESULTRESPONSE.fields_by_name['result'].containing_oneof = _PROPOSERESULTRESPONSE.oneofs_by_name['message']
DESCRIPTOR.message_types_by_name['ProposeResponse'] = _PROPOSERESPONSE
DESCRIPTOR.message_types_by_name['ProposeResultResponse'] = _PROPOSERESULTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProposeResponse = _reflection.GeneratedProtocolMessageType('ProposeResponse', (_message.Message,), {
  'DESCRIPTOR' : _PROPOSERESPONSE,
  '__module__' : 'ProposeServiceV1_pb2'
  # @@protoc_insertion_point(class_scope:casper.v1.ProposeResponse)
  })
_sym_db.RegisterMessage(ProposeResponse)

ProposeResultResponse = _reflection.GeneratedProtocolMessageType('ProposeResultResponse', (_message.Message,), {
  'DESCRIPTOR' : _PROPOSERESULTRESPONSE,
  '__module__' : 'ProposeServiceV1_pb2'
  # @@protoc_insertion_point(class_scope:casper.v1.ProposeResultResponse)
  })
_sym_db.RegisterMessage(ProposeResultResponse)


DESCRIPTOR._options = None

_PROPOSESERVICE = _descriptor.ServiceDescriptor(
  name='ProposeService',
  full_name='casper.v1.ProposeService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=275,
  serialized_end=447,
  methods=[
  _descriptor.MethodDescriptor(
    name='propose',
    full_name='casper.v1.ProposeService.propose',
    index=0,
    containing_service=None,
    input_type=ProposeServiceCommon__pb2._PRINTUNMATCHEDSENDSQUERY,
    output_type=_PROPOSERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='proposeResult',
    full_name='casper.v1.ProposeService.proposeResult',
    index=1,
    containing_service=None,
    input_type=ProposeServiceCommon__pb2._PROPOSERESULTQUERY,
    output_type=_PROPOSERESULTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PROPOSESERVICE)

DESCRIPTOR.services_by_name['ProposeService'] = _PROPOSESERVICE

# @@protoc_insertion_point(module_scope)

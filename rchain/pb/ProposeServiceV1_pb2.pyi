# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from .ServiceError_pb2 import (
    ServiceError as ServiceError_pb2___ServiceError,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class ProposeResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    result: typing___Text = ...

    @property
    def error(self) -> ServiceError_pb2___ServiceError: ...

    def __init__(self,
        *,
        error : typing___Optional[ServiceError_pb2___ServiceError] = None,
        result : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"error",b"error",u"message",b"message",u"result",b"result"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"error",b"error",u"message",b"message",u"result",b"result"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"message",b"message"]) -> typing_extensions___Literal["error","result"]: ...
type___ProposeResponse = ProposeResponse

class ProposeResultResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    result: typing___Text = ...

    @property
    def error(self) -> ServiceError_pb2___ServiceError: ...

    def __init__(self,
        *,
        error : typing___Optional[ServiceError_pb2___ServiceError] = None,
        result : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"error",b"error",u"message",b"message",u"result",b"result"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"error",b"error",u"message",b"message",u"result",b"result"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"message",b"message"]) -> typing_extensions___Literal["error","result"]: ...
type___ProposeResultResponse = ProposeResultResponse

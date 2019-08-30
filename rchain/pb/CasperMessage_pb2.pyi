# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from .RhoTypes_pb2 import (
    PCost as RhoTypes_pb2___PCost,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class HasBlockRequest(google___protobuf___message___Message):
    hash = ... # type: bytes

    def __init__(self,
        *,
        hash : typing___Optional[bytes] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> HasBlockRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"hash"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"hash",b"hash"]) -> None: ...

class HasBlock(google___protobuf___message___Message):
    hash = ... # type: bytes

    def __init__(self,
        *,
        hash : typing___Optional[bytes] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> HasBlock: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"hash"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"hash",b"hash"]) -> None: ...

class BlockRequest(google___protobuf___message___Message):
    hash = ... # type: bytes

    def __init__(self,
        *,
        hash : typing___Optional[bytes] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BlockRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"hash"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"hash",b"hash"]) -> None: ...

class ForkChoiceTipRequest(google___protobuf___message___Message):

    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ForkChoiceTipRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class ApprovedBlockCandidate(google___protobuf___message___Message):
    requiredSigs = ... # type: int

    @property
    def block(self) -> BlockMessage: ...

    def __init__(self,
        *,
        block : typing___Optional[BlockMessage] = None,
        requiredSigs : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ApprovedBlockCandidate: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"block"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"block",u"requiredSigs"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"block",b"block"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"block",b"block",u"requiredSigs",b"requiredSigs"]) -> None: ...

class UnapprovedBlock(google___protobuf___message___Message):
    timestamp = ... # type: int
    duration = ... # type: int

    @property
    def candidate(self) -> ApprovedBlockCandidate: ...

    def __init__(self,
        *,
        candidate : typing___Optional[ApprovedBlockCandidate] = None,
        timestamp : typing___Optional[int] = None,
        duration : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> UnapprovedBlock: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"candidate"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"candidate",u"duration",u"timestamp"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"candidate",b"candidate"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"candidate",b"candidate",u"duration",b"duration",u"timestamp",b"timestamp"]) -> None: ...

class Signature(google___protobuf___message___Message):
    publicKey = ... # type: bytes
    algorithm = ... # type: typing___Text
    sig = ... # type: bytes

    def __init__(self,
        *,
        publicKey : typing___Optional[bytes] = None,
        algorithm : typing___Optional[typing___Text] = None,
        sig : typing___Optional[bytes] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Signature: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"algorithm",u"publicKey",u"sig"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"algorithm",b"algorithm",u"publicKey",b"publicKey",u"sig",b"sig"]) -> None: ...

class BlockApproval(google___protobuf___message___Message):

    @property
    def candidate(self) -> ApprovedBlockCandidate: ...

    @property
    def sig(self) -> Signature: ...

    def __init__(self,
        *,
        candidate : typing___Optional[ApprovedBlockCandidate] = None,
        sig : typing___Optional[Signature] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BlockApproval: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"candidate",u"sig"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"candidate",u"sig"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"candidate",b"candidate",u"sig",b"sig"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"candidate",b"candidate",u"sig",b"sig"]) -> None: ...

class ApprovedBlock(google___protobuf___message___Message):

    @property
    def candidate(self) -> ApprovedBlockCandidate: ...

    @property
    def sigs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Signature]: ...

    def __init__(self,
        *,
        candidate : typing___Optional[ApprovedBlockCandidate] = None,
        sigs : typing___Optional[typing___Iterable[Signature]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ApprovedBlock: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"candidate"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"candidate",u"sigs"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"candidate",b"candidate"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"candidate",b"candidate",u"sigs",b"sigs"]) -> None: ...

class ApprovedBlockRequest(google___protobuf___message___Message):
    identifier = ... # type: typing___Text

    def __init__(self,
        *,
        identifier : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ApprovedBlockRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"identifier"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"identifier",b"identifier"]) -> None: ...

class NoApprovedBlockAvailable(google___protobuf___message___Message):
    identifier = ... # type: typing___Text
    nodeIdentifer = ... # type: typing___Text

    def __init__(self,
        *,
        identifier : typing___Optional[typing___Text] = None,
        nodeIdentifer : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> NoApprovedBlockAvailable: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"identifier",u"nodeIdentifer"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"identifier",b"identifier",u"nodeIdentifer",b"nodeIdentifer"]) -> None: ...

class BlockMessage(google___protobuf___message___Message):
    blockHash = ... # type: bytes
    sender = ... # type: bytes
    seqNum = ... # type: int
    sig = ... # type: bytes
    sigAlgorithm = ... # type: typing___Text
    shardId = ... # type: typing___Text
    extraBytes = ... # type: bytes

    @property
    def header(self) -> Header: ...

    @property
    def body(self) -> Body: ...

    @property
    def justifications(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Justification]: ...

    def __init__(self,
        *,
        blockHash : typing___Optional[bytes] = None,
        header : typing___Optional[Header] = None,
        body : typing___Optional[Body] = None,
        justifications : typing___Optional[typing___Iterable[Justification]] = None,
        sender : typing___Optional[bytes] = None,
        seqNum : typing___Optional[int] = None,
        sig : typing___Optional[bytes] = None,
        sigAlgorithm : typing___Optional[typing___Text] = None,
        shardId : typing___Optional[typing___Text] = None,
        extraBytes : typing___Optional[bytes] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BlockMessage: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"body",u"header"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"blockHash",u"body",u"extraBytes",u"header",u"justifications",u"sender",u"seqNum",u"shardId",u"sig",u"sigAlgorithm"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"body",b"body",u"header",b"header"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"blockHash",b"blockHash",u"body",b"body",u"extraBytes",b"extraBytes",u"header",b"header",u"justifications",b"justifications",u"sender",b"sender",u"seqNum",b"seqNum",u"shardId",b"shardId",u"sig",b"sig",u"sigAlgorithm",b"sigAlgorithm"]) -> None: ...

class BlockMetadataInternal(google___protobuf___message___Message):
    blockHash = ... # type: bytes
    parents = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[bytes]
    sender = ... # type: bytes
    blockNum = ... # type: int
    seqNum = ... # type: int
    invalid = ... # type: bool

    @property
    def justifications(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Justification]: ...

    @property
    def bonds(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Bond]: ...

    def __init__(self,
        *,
        blockHash : typing___Optional[bytes] = None,
        parents : typing___Optional[typing___Iterable[bytes]] = None,
        sender : typing___Optional[bytes] = None,
        justifications : typing___Optional[typing___Iterable[Justification]] = None,
        bonds : typing___Optional[typing___Iterable[Bond]] = None,
        blockNum : typing___Optional[int] = None,
        seqNum : typing___Optional[int] = None,
        invalid : typing___Optional[bool] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BlockMetadataInternal: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"blockHash",u"blockNum",u"bonds",u"invalid",u"justifications",u"parents",u"sender",u"seqNum"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"blockHash",b"blockHash",u"blockNum",b"blockNum",u"bonds",b"bonds",u"invalid",b"invalid",u"justifications",b"justifications",u"parents",b"parents",u"sender",b"sender",u"seqNum",b"seqNum"]) -> None: ...

class Header(google___protobuf___message___Message):
    parentsHashList = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[bytes]
    deploysHash = ... # type: bytes
    timestamp = ... # type: int
    version = ... # type: int
    deployCount = ... # type: int
    extraBytes = ... # type: bytes

    def __init__(self,
        *,
        parentsHashList : typing___Optional[typing___Iterable[bytes]] = None,
        deploysHash : typing___Optional[bytes] = None,
        timestamp : typing___Optional[int] = None,
        version : typing___Optional[int] = None,
        deployCount : typing___Optional[int] = None,
        extraBytes : typing___Optional[bytes] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Header: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"deployCount",u"deploysHash",u"extraBytes",u"parentsHashList",u"timestamp",u"version"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"deployCount",b"deployCount",u"deploysHash",b"deploysHash",u"extraBytes",b"extraBytes",u"parentsHashList",b"parentsHashList",u"timestamp",b"timestamp",u"version",b"version"]) -> None: ...

class DeployData(google___protobuf___message___Message):
    deployer = ... # type: bytes
    term = ... # type: typing___Text
    timestamp = ... # type: int
    sig = ... # type: bytes
    sigAlgorithm = ... # type: typing___Text
    phloPrice = ... # type: int
    phloLimit = ... # type: int
    validAfterBlockNumber = ... # type: int

    def __init__(self,
        *,
        deployer : typing___Optional[bytes] = None,
        term : typing___Optional[typing___Text] = None,
        timestamp : typing___Optional[int] = None,
        sig : typing___Optional[bytes] = None,
        sigAlgorithm : typing___Optional[typing___Text] = None,
        phloPrice : typing___Optional[int] = None,
        phloLimit : typing___Optional[int] = None,
        validAfterBlockNumber : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> DeployData: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"deployer",u"phloLimit",u"phloPrice",u"sig",u"sigAlgorithm",u"term",u"timestamp",u"validAfterBlockNumber"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"deployer",b"deployer",u"phloLimit",b"phloLimit",u"phloPrice",b"phloPrice",u"sig",b"sig",u"sigAlgorithm",b"sigAlgorithm",u"term",b"term",u"timestamp",b"timestamp",u"validAfterBlockNumber",b"validAfterBlockNumber"]) -> None: ...

class ProcessedDeploy(google___protobuf___message___Message):
    errored = ... # type: bool

    @property
    def deploy(self) -> DeployData: ...

    @property
    def cost(self) -> RhoTypes_pb2___PCost: ...

    @property
    def deployLog(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Event]: ...

    @property
    def paymentLog(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Event]: ...

    def __init__(self,
        *,
        deploy : typing___Optional[DeployData] = None,
        cost : typing___Optional[RhoTypes_pb2___PCost] = None,
        deployLog : typing___Optional[typing___Iterable[Event]] = None,
        paymentLog : typing___Optional[typing___Iterable[Event]] = None,
        errored : typing___Optional[bool] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ProcessedDeploy: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"cost",u"deploy"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"cost",u"deploy",u"deployLog",u"errored",u"paymentLog"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"cost",b"cost",u"deploy",b"deploy"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"cost",b"cost",u"deploy",b"deploy",u"deployLog",b"deployLog",u"errored",b"errored",u"paymentLog",b"paymentLog"]) -> None: ...

class Body(google___protobuf___message___Message):
    extraBytes = ... # type: bytes

    @property
    def state(self) -> RChainState: ...

    @property
    def deploys(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ProcessedDeploy]: ...

    def __init__(self,
        *,
        state : typing___Optional[RChainState] = None,
        deploys : typing___Optional[typing___Iterable[ProcessedDeploy]] = None,
        extraBytes : typing___Optional[bytes] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Body: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"state"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"deploys",u"extraBytes",u"state"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"state",b"state"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"deploys",b"deploys",u"extraBytes",b"extraBytes",u"state",b"state"]) -> None: ...

class Justification(google___protobuf___message___Message):
    validator = ... # type: bytes
    latestBlockHash = ... # type: bytes

    def __init__(self,
        *,
        validator : typing___Optional[bytes] = None,
        latestBlockHash : typing___Optional[bytes] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Justification: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"latestBlockHash",u"validator"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"latestBlockHash",b"latestBlockHash",u"validator",b"validator"]) -> None: ...

class RChainState(google___protobuf___message___Message):
    preStateHash = ... # type: bytes
    postStateHash = ... # type: bytes
    blockNumber = ... # type: int

    @property
    def bonds(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Bond]: ...

    def __init__(self,
        *,
        preStateHash : typing___Optional[bytes] = None,
        postStateHash : typing___Optional[bytes] = None,
        bonds : typing___Optional[typing___Iterable[Bond]] = None,
        blockNumber : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> RChainState: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"blockNumber",u"bonds",u"postStateHash",u"preStateHash"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"blockNumber",b"blockNumber",u"bonds",b"bonds",u"postStateHash",b"postStateHash",u"preStateHash",b"preStateHash"]) -> None: ...

class Event(google___protobuf___message___Message):

    @property
    def produce(self) -> ProduceEvent: ...

    @property
    def consume(self) -> ConsumeEvent: ...

    @property
    def comm(self) -> CommEvent: ...

    def __init__(self,
        *,
        produce : typing___Optional[ProduceEvent] = None,
        consume : typing___Optional[ConsumeEvent] = None,
        comm : typing___Optional[CommEvent] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Event: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"comm",u"consume",u"event_instance",u"produce"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"comm",u"consume",u"event_instance",u"produce"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"comm",b"comm",u"consume",b"consume",u"event_instance",b"event_instance",u"produce",b"produce"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"comm",b"comm",u"consume",b"consume",u"event_instance",b"event_instance",u"produce",b"produce"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"event_instance",b"event_instance"]) -> typing_extensions___Literal["produce","consume","comm"]: ...

class ProduceEvent(google___protobuf___message___Message):
    channelsHash = ... # type: bytes
    hash = ... # type: bytes
    persistent = ... # type: bool
    sequenceNumber = ... # type: int

    def __init__(self,
        *,
        channelsHash : typing___Optional[bytes] = None,
        hash : typing___Optional[bytes] = None,
        persistent : typing___Optional[bool] = None,
        sequenceNumber : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ProduceEvent: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"channelsHash",u"hash",u"persistent",u"sequenceNumber"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"channelsHash",b"channelsHash",u"hash",b"hash",u"persistent",b"persistent",u"sequenceNumber",b"sequenceNumber"]) -> None: ...

class ConsumeEvent(google___protobuf___message___Message):
    channelsHashes = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[bytes]
    hash = ... # type: bytes
    persistent = ... # type: bool
    sequenceNumber = ... # type: int

    def __init__(self,
        *,
        channelsHashes : typing___Optional[typing___Iterable[bytes]] = None,
        hash : typing___Optional[bytes] = None,
        persistent : typing___Optional[bool] = None,
        sequenceNumber : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ConsumeEvent: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"channelsHashes",u"hash",u"persistent",u"sequenceNumber"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"channelsHashes",b"channelsHashes",u"hash",b"hash",u"persistent",b"persistent",u"sequenceNumber",b"sequenceNumber"]) -> None: ...

class CommEvent(google___protobuf___message___Message):

    @property
    def consume(self) -> ConsumeEvent: ...

    @property
    def produces(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ProduceEvent]: ...

    @property
    def peeks(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Peek]: ...

    def __init__(self,
        *,
        consume : typing___Optional[ConsumeEvent] = None,
        produces : typing___Optional[typing___Iterable[ProduceEvent]] = None,
        peeks : typing___Optional[typing___Iterable[Peek]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CommEvent: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"consume"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"consume",u"peeks",u"produces"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"consume",b"consume"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"consume",b"consume",u"peeks",b"peeks",u"produces",b"produces"]) -> None: ...

class Peek(google___protobuf___message___Message):
    channelIndex = ... # type: int

    def __init__(self,
        *,
        channelIndex : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Peek: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"channelIndex"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"channelIndex",b"channelIndex"]) -> None: ...

class Bond(google___protobuf___message___Message):
    validator = ... # type: bytes
    stake = ... # type: int

    def __init__(self,
        *,
        validator : typing___Optional[bytes] = None,
        stake : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Bond: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"stake",u"validator"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"stake",b"stake",u"validator",b"validator"]) -> None: ...

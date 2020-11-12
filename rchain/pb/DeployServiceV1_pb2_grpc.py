# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import CasperMessage_pb2 as CasperMessage__pb2
from . import DeployServiceCommon_pb2 as DeployServiceCommon__pb2
from . import DeployServiceV1_pb2 as DeployServiceV1__pb2


class DeployServiceStub(object):
    """Use `doDeploy` to queue deployments of Rholang code and then
    `ProposeServiceV2.propose` to make a new block with the results of running them
    all.

    To get results back, use `listenForDataAtName`.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.doDeploy = channel.unary_unary(
                '/casper.v1.DeployService/doDeploy',
                request_serializer=CasperMessage__pb2.DeployDataProto.SerializeToString,
                response_deserializer=DeployServiceV1__pb2.DeployResponse.FromString,
                )
        self.getBlock = channel.unary_unary(
                '/casper.v1.DeployService/getBlock',
                request_serializer=DeployServiceCommon__pb2.BlockQuery.SerializeToString,
                response_deserializer=DeployServiceV1__pb2.BlockResponse.FromString,
                )
        self.visualizeDag = channel.unary_stream(
                '/casper.v1.DeployService/visualizeDag',
                request_serializer=DeployServiceCommon__pb2.VisualizeDagQuery.SerializeToString,
                response_deserializer=DeployServiceV1__pb2.VisualizeBlocksResponse.FromString,
                )
        self.machineVerifiableDag = channel.unary_unary(
                '/casper.v1.DeployService/machineVerifiableDag',
                request_serializer=DeployServiceCommon__pb2.MachineVerifyQuery.SerializeToString,
                response_deserializer=DeployServiceV1__pb2.MachineVerifyResponse.FromString,
                )
        self.showMainChain = channel.unary_stream(
                '/casper.v1.DeployService/showMainChain',
                request_serializer=DeployServiceCommon__pb2.BlocksQuery.SerializeToString,
                response_deserializer=DeployServiceV1__pb2.BlockInfoResponse.FromString,
                )
        self.getBlocks = channel.unary_stream(
                '/casper.v1.DeployService/getBlocks',
                request_serializer=DeployServiceCommon__pb2.BlocksQuery.SerializeToString,
                response_deserializer=DeployServiceV1__pb2.BlockInfoResponse.FromString,
                )
        self.listenForDataAtName = channel.unary_unary(
                '/casper.v1.DeployService/listenForDataAtName',
                request_serializer=DeployServiceCommon__pb2.DataAtNameQuery.SerializeToString,
                response_deserializer=DeployServiceV1__pb2.ListeningNameDataResponse.FromString,
                )
        self.listenForContinuationAtName = channel.unary_unary(
                '/casper.v1.DeployService/listenForContinuationAtName',
                request_serializer=DeployServiceCommon__pb2.ContinuationAtNameQuery.SerializeToString,
                response_deserializer=DeployServiceV1__pb2.ContinuationAtNameResponse.FromString,
                )
        self.findDeploy = channel.unary_unary(
                '/casper.v1.DeployService/findDeploy',
                request_serializer=DeployServiceCommon__pb2.FindDeployQuery.SerializeToString,
                response_deserializer=DeployServiceV1__pb2.FindDeployResponse.FromString,
                )
        self.previewPrivateNames = channel.unary_unary(
                '/casper.v1.DeployService/previewPrivateNames',
                request_serializer=DeployServiceCommon__pb2.PrivateNamePreviewQuery.SerializeToString,
                response_deserializer=DeployServiceV1__pb2.PrivateNamePreviewResponse.FromString,
                )
        self.lastFinalizedBlock = channel.unary_unary(
                '/casper.v1.DeployService/lastFinalizedBlock',
                request_serializer=DeployServiceCommon__pb2.LastFinalizedBlockQuery.SerializeToString,
                response_deserializer=DeployServiceV1__pb2.LastFinalizedBlockResponse.FromString,
                )
        self.isFinalized = channel.unary_unary(
                '/casper.v1.DeployService/isFinalized',
                request_serializer=DeployServiceCommon__pb2.IsFinalizedQuery.SerializeToString,
                response_deserializer=DeployServiceV1__pb2.IsFinalizedResponse.FromString,
                )
        self.bondStatus = channel.unary_unary(
                '/casper.v1.DeployService/bondStatus',
                request_serializer=DeployServiceCommon__pb2.BondStatusQuery.SerializeToString,
                response_deserializer=DeployServiceV1__pb2.BondStatusResponse.FromString,
                )
        self.exploratoryDeploy = channel.unary_unary(
                '/casper.v1.DeployService/exploratoryDeploy',
                request_serializer=DeployServiceCommon__pb2.ExploratoryDeployQuery.SerializeToString,
                response_deserializer=DeployServiceV1__pb2.ExploratoryDeployResponse.FromString,
                )
        self.getBlocksByHeights = channel.unary_stream(
                '/casper.v1.DeployService/getBlocksByHeights',
                request_serializer=DeployServiceCommon__pb2.BlocksQueryByHeight.SerializeToString,
                response_deserializer=DeployServiceV1__pb2.BlockInfoResponse.FromString,
                )
        self.getEventByHash = channel.unary_unary(
                '/casper.v1.DeployService/getEventByHash',
                request_serializer=DeployServiceCommon__pb2.BlockQuery.SerializeToString,
                response_deserializer=DeployServiceV1__pb2.EventInfoResponse.FromString,
                )


class DeployServiceServicer(object):
    """Use `doDeploy` to queue deployments of Rholang code and then
    `ProposeServiceV2.propose` to make a new block with the results of running them
    all.

    To get results back, use `listenForDataAtName`.
    """

    def doDeploy(self, request, context):
        """Queue deployment of Rholang code (or fail to parse).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getBlock(self, request, context):
        """Get details about a particular block.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def visualizeDag(self, request, context):
        """Get dag
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def machineVerifiableDag(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def showMainChain(self, request, context):
        """Returns on success LightBlockInfo
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getBlocks(self, request, context):
        """Get a summary of blocks on the blockchain.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def listenForDataAtName(self, request, context):
        """Find data sent to a name.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def listenForContinuationAtName(self, request, context):
        """Find processes receiving on a name.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def findDeploy(self, request, context):
        """Find block containing a deploy.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def previewPrivateNames(self, request, context):
        """Preview new top-level unforgeable names (for example, to compute signatures over them).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def lastFinalizedBlock(self, request, context):
        """Get details about a particular block.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def isFinalized(self, request, context):
        """Check if a given block is finalized.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def bondStatus(self, request, context):
        """Check if a given validator is bonded.
        Returns on success BondStatusResponse
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def exploratoryDeploy(self, request, context):
        """Executes deploy as user deploy with immediate rollback and return result
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getBlocksByHeights(self, request, context):
        """get blocks by block height
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getEventByHash(self, request, context):
        """temporary api for testing
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DeployServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'doDeploy': grpc.unary_unary_rpc_method_handler(
                    servicer.doDeploy,
                    request_deserializer=CasperMessage__pb2.DeployDataProto.FromString,
                    response_serializer=DeployServiceV1__pb2.DeployResponse.SerializeToString,
            ),
            'getBlock': grpc.unary_unary_rpc_method_handler(
                    servicer.getBlock,
                    request_deserializer=DeployServiceCommon__pb2.BlockQuery.FromString,
                    response_serializer=DeployServiceV1__pb2.BlockResponse.SerializeToString,
            ),
            'visualizeDag': grpc.unary_stream_rpc_method_handler(
                    servicer.visualizeDag,
                    request_deserializer=DeployServiceCommon__pb2.VisualizeDagQuery.FromString,
                    response_serializer=DeployServiceV1__pb2.VisualizeBlocksResponse.SerializeToString,
            ),
            'machineVerifiableDag': grpc.unary_unary_rpc_method_handler(
                    servicer.machineVerifiableDag,
                    request_deserializer=DeployServiceCommon__pb2.MachineVerifyQuery.FromString,
                    response_serializer=DeployServiceV1__pb2.MachineVerifyResponse.SerializeToString,
            ),
            'showMainChain': grpc.unary_stream_rpc_method_handler(
                    servicer.showMainChain,
                    request_deserializer=DeployServiceCommon__pb2.BlocksQuery.FromString,
                    response_serializer=DeployServiceV1__pb2.BlockInfoResponse.SerializeToString,
            ),
            'getBlocks': grpc.unary_stream_rpc_method_handler(
                    servicer.getBlocks,
                    request_deserializer=DeployServiceCommon__pb2.BlocksQuery.FromString,
                    response_serializer=DeployServiceV1__pb2.BlockInfoResponse.SerializeToString,
            ),
            'listenForDataAtName': grpc.unary_unary_rpc_method_handler(
                    servicer.listenForDataAtName,
                    request_deserializer=DeployServiceCommon__pb2.DataAtNameQuery.FromString,
                    response_serializer=DeployServiceV1__pb2.ListeningNameDataResponse.SerializeToString,
            ),
            'listenForContinuationAtName': grpc.unary_unary_rpc_method_handler(
                    servicer.listenForContinuationAtName,
                    request_deserializer=DeployServiceCommon__pb2.ContinuationAtNameQuery.FromString,
                    response_serializer=DeployServiceV1__pb2.ContinuationAtNameResponse.SerializeToString,
            ),
            'findDeploy': grpc.unary_unary_rpc_method_handler(
                    servicer.findDeploy,
                    request_deserializer=DeployServiceCommon__pb2.FindDeployQuery.FromString,
                    response_serializer=DeployServiceV1__pb2.FindDeployResponse.SerializeToString,
            ),
            'previewPrivateNames': grpc.unary_unary_rpc_method_handler(
                    servicer.previewPrivateNames,
                    request_deserializer=DeployServiceCommon__pb2.PrivateNamePreviewQuery.FromString,
                    response_serializer=DeployServiceV1__pb2.PrivateNamePreviewResponse.SerializeToString,
            ),
            'lastFinalizedBlock': grpc.unary_unary_rpc_method_handler(
                    servicer.lastFinalizedBlock,
                    request_deserializer=DeployServiceCommon__pb2.LastFinalizedBlockQuery.FromString,
                    response_serializer=DeployServiceV1__pb2.LastFinalizedBlockResponse.SerializeToString,
            ),
            'isFinalized': grpc.unary_unary_rpc_method_handler(
                    servicer.isFinalized,
                    request_deserializer=DeployServiceCommon__pb2.IsFinalizedQuery.FromString,
                    response_serializer=DeployServiceV1__pb2.IsFinalizedResponse.SerializeToString,
            ),
            'bondStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.bondStatus,
                    request_deserializer=DeployServiceCommon__pb2.BondStatusQuery.FromString,
                    response_serializer=DeployServiceV1__pb2.BondStatusResponse.SerializeToString,
            ),
            'exploratoryDeploy': grpc.unary_unary_rpc_method_handler(
                    servicer.exploratoryDeploy,
                    request_deserializer=DeployServiceCommon__pb2.ExploratoryDeployQuery.FromString,
                    response_serializer=DeployServiceV1__pb2.ExploratoryDeployResponse.SerializeToString,
            ),
            'getBlocksByHeights': grpc.unary_stream_rpc_method_handler(
                    servicer.getBlocksByHeights,
                    request_deserializer=DeployServiceCommon__pb2.BlocksQueryByHeight.FromString,
                    response_serializer=DeployServiceV1__pb2.BlockInfoResponse.SerializeToString,
            ),
            'getEventByHash': grpc.unary_unary_rpc_method_handler(
                    servicer.getEventByHash,
                    request_deserializer=DeployServiceCommon__pb2.BlockQuery.FromString,
                    response_serializer=DeployServiceV1__pb2.EventInfoResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'casper.v1.DeployService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DeployService(object):
    """Use `doDeploy` to queue deployments of Rholang code and then
    `ProposeServiceV2.propose` to make a new block with the results of running them
    all.

    To get results back, use `listenForDataAtName`.
    """

    @staticmethod
    def doDeploy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/casper.v1.DeployService/doDeploy',
            CasperMessage__pb2.DeployDataProto.SerializeToString,
            DeployServiceV1__pb2.DeployResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getBlock(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/casper.v1.DeployService/getBlock',
            DeployServiceCommon__pb2.BlockQuery.SerializeToString,
            DeployServiceV1__pb2.BlockResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def visualizeDag(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/casper.v1.DeployService/visualizeDag',
            DeployServiceCommon__pb2.VisualizeDagQuery.SerializeToString,
            DeployServiceV1__pb2.VisualizeBlocksResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def machineVerifiableDag(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/casper.v1.DeployService/machineVerifiableDag',
            DeployServiceCommon__pb2.MachineVerifyQuery.SerializeToString,
            DeployServiceV1__pb2.MachineVerifyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def showMainChain(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/casper.v1.DeployService/showMainChain',
            DeployServiceCommon__pb2.BlocksQuery.SerializeToString,
            DeployServiceV1__pb2.BlockInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getBlocks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/casper.v1.DeployService/getBlocks',
            DeployServiceCommon__pb2.BlocksQuery.SerializeToString,
            DeployServiceV1__pb2.BlockInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def listenForDataAtName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/casper.v1.DeployService/listenForDataAtName',
            DeployServiceCommon__pb2.DataAtNameQuery.SerializeToString,
            DeployServiceV1__pb2.ListeningNameDataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def listenForContinuationAtName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/casper.v1.DeployService/listenForContinuationAtName',
            DeployServiceCommon__pb2.ContinuationAtNameQuery.SerializeToString,
            DeployServiceV1__pb2.ContinuationAtNameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def findDeploy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/casper.v1.DeployService/findDeploy',
            DeployServiceCommon__pb2.FindDeployQuery.SerializeToString,
            DeployServiceV1__pb2.FindDeployResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def previewPrivateNames(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/casper.v1.DeployService/previewPrivateNames',
            DeployServiceCommon__pb2.PrivateNamePreviewQuery.SerializeToString,
            DeployServiceV1__pb2.PrivateNamePreviewResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def lastFinalizedBlock(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/casper.v1.DeployService/lastFinalizedBlock',
            DeployServiceCommon__pb2.LastFinalizedBlockQuery.SerializeToString,
            DeployServiceV1__pb2.LastFinalizedBlockResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def isFinalized(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/casper.v1.DeployService/isFinalized',
            DeployServiceCommon__pb2.IsFinalizedQuery.SerializeToString,
            DeployServiceV1__pb2.IsFinalizedResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def bondStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/casper.v1.DeployService/bondStatus',
            DeployServiceCommon__pb2.BondStatusQuery.SerializeToString,
            DeployServiceV1__pb2.BondStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def exploratoryDeploy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/casper.v1.DeployService/exploratoryDeploy',
            DeployServiceCommon__pb2.ExploratoryDeployQuery.SerializeToString,
            DeployServiceV1__pb2.ExploratoryDeployResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getBlocksByHeights(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/casper.v1.DeployService/getBlocksByHeights',
            DeployServiceCommon__pb2.BlocksQueryByHeight.SerializeToString,
            DeployServiceV1__pb2.BlockInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getEventByHash(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/casper.v1.DeployService/getEventByHash',
            DeployServiceCommon__pb2.BlockQuery.SerializeToString,
            DeployServiceV1__pb2.EventInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

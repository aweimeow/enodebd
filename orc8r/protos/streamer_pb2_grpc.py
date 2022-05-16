# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from orc8r.protos import streamer_pb2 as orc8r_dot_protos_dot_streamer__pb2


class StreamerStub(object):
    """Streamer provides a pipeline for the cloud to push the updates to the
    gateway as and when the update happens.

    The Streamer interface defines the semantics and consistency guarantees
    between the cloud and the gateway while abstracting the details of how
    it's implemented in the cloud and what the gateway does with the updates.

    - The gateways call the GetUpdates() streaming API with a StreamRequest
    indicating the stream name and the offset to continue streaming from.
    - The cloud sends a stream of DataUpdateBatch containing a batch of updates.
    - If resync is true, then the gateway can cleanup all its data and add
    all the keys (the batch is guaranteed to contain only unique keys).
    - If resync is false, then the gateway can update the keys, or add new
    ones if the key is not already present.
    - Key deletions are not yet supported (#15109350)
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetUpdates = channel.unary_stream(
                '/magma.orc8r.Streamer/GetUpdates',
                request_serializer=orc8r_dot_protos_dot_streamer__pb2.StreamRequest.SerializeToString,
                response_deserializer=orc8r_dot_protos_dot_streamer__pb2.DataUpdateBatch.FromString,
                )


class StreamerServicer(object):
    """Streamer provides a pipeline for the cloud to push the updates to the
    gateway as and when the update happens.

    The Streamer interface defines the semantics and consistency guarantees
    between the cloud and the gateway while abstracting the details of how
    it's implemented in the cloud and what the gateway does with the updates.

    - The gateways call the GetUpdates() streaming API with a StreamRequest
    indicating the stream name and the offset to continue streaming from.
    - The cloud sends a stream of DataUpdateBatch containing a batch of updates.
    - If resync is true, then the gateway can cleanup all its data and add
    all the keys (the batch is guaranteed to contain only unique keys).
    - If resync is false, then the gateway can update the keys, or add new
    ones if the key is not already present.
    - Key deletions are not yet supported (#15109350)
    """

    def GetUpdates(self, request, context):
        """GetUpdates streams config updates from the cloud.
        The RPC call would be kept open to push new updates as they happen.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StreamerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetUpdates': grpc.unary_stream_rpc_method_handler(
                    servicer.GetUpdates,
                    request_deserializer=orc8r_dot_protos_dot_streamer__pb2.StreamRequest.FromString,
                    response_serializer=orc8r_dot_protos_dot_streamer__pb2.DataUpdateBatch.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'magma.orc8r.Streamer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Streamer(object):
    """Streamer provides a pipeline for the cloud to push the updates to the
    gateway as and when the update happens.

    The Streamer interface defines the semantics and consistency guarantees
    between the cloud and the gateway while abstracting the details of how
    it's implemented in the cloud and what the gateway does with the updates.

    - The gateways call the GetUpdates() streaming API with a StreamRequest
    indicating the stream name and the offset to continue streaming from.
    - The cloud sends a stream of DataUpdateBatch containing a batch of updates.
    - If resync is true, then the gateway can cleanup all its data and add
    all the keys (the batch is guaranteed to contain only unique keys).
    - If resync is false, then the gateway can update the keys, or add new
    ones if the key is not already present.
    - Key deletions are not yet supported (#15109350)
    """

    @staticmethod
    def GetUpdates(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/magma.orc8r.Streamer/GetUpdates',
            orc8r_dot_protos_dot_streamer__pb2.StreamRequest.SerializeToString,
            orc8r_dot_protos_dot_streamer__pb2.DataUpdateBatch.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
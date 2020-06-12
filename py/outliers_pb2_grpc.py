# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import outliers_pb2 as outliers__pb2


class OutliersStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Detect = channel.unary_unary(
                '/pb.Outliers/Detect',
                request_serializer=outliers__pb2.OutliersRequest.SerializeToString,
                response_deserializer=outliers__pb2.OutliersResponse.FromString,
                )


class OutliersServicer(object):
    """Missing associated documentation comment in .proto file"""

    def Detect(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OutliersServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Detect': grpc.unary_unary_rpc_method_handler(
                    servicer.Detect,
                    request_deserializer=outliers__pb2.OutliersRequest.FromString,
                    response_serializer=outliers__pb2.OutliersResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pb.Outliers', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Outliers(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def Detect(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.Outliers/Detect',
            outliers__pb2.OutliersRequest.SerializeToString,
            outliers__pb2.OutliersResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

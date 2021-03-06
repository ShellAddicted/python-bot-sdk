# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import integrations_pb2 as integrations__pb2


class IntegrationsStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetIntegrationToken = channel.unary_unary(
        '/dialog.Integrations/GetIntegrationToken',
        request_serializer=integrations__pb2.RequestGetIntegrationToken.SerializeToString,
        response_deserializer=integrations__pb2.ResponseIntegrationToken.FromString,
        )
    self.RevokeIntegrationToken = channel.unary_unary(
        '/dialog.Integrations/RevokeIntegrationToken',
        request_serializer=integrations__pb2.RequestRevokeIntegrationToken.SerializeToString,
        response_deserializer=integrations__pb2.ResponseIntegrationToken.FromString,
        )


class IntegrationsServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetIntegrationToken(self, request, context):
    """/ Get token for posting to group
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RevokeIntegrationToken(self, request, context):
    """/ Revoke token
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_IntegrationsServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetIntegrationToken': grpc.unary_unary_rpc_method_handler(
          servicer.GetIntegrationToken,
          request_deserializer=integrations__pb2.RequestGetIntegrationToken.FromString,
          response_serializer=integrations__pb2.ResponseIntegrationToken.SerializeToString,
      ),
      'RevokeIntegrationToken': grpc.unary_unary_rpc_method_handler(
          servicer.RevokeIntegrationToken,
          request_deserializer=integrations__pb2.RequestRevokeIntegrationToken.FromString,
          response_serializer=integrations__pb2.ResponseIntegrationToken.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'dialog.Integrations', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

from typing import List
from aws_cdk.core import App, Stack, Environment, Construct, NestedStack

class ILandingZone(Stack):
  """
  Define a deployment instance
  """
  def __init__(self, scope:Construct, id:str, **kwargs)->None:
    super().__init__(scope, id, **kwargs)

  @property
  def zone_name(self)->str:
    raise NotImplementedError()
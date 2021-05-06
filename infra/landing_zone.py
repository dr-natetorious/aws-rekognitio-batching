#!/usr/bin/env python3
import os.path
from typing import List
from aws_cdk.core import App, Stack, Environment, Construct, NestedStack
from aws_cdk import (
    core,
    aws_ec2 as ec2,
)

class ILandingZone(Stack):
  """
  Define a deployment instance
  """
  def __init__(self, scope:Construct, id:str, **kwargs)->None:
    super().__init__(scope, id, **kwargs)

  @property
  def zone_name(self)->str:
    raise NotImplementedError()

#!/usr/bin/env python3
import os.path
from typing import List
from infra.backup import BackupStrategyConstruct
from infra.interfaces import ILandingZone
from infra.storage import StorageConstruct
from aws_cdk.core import App, Stack, Environment, Construct, NestedStack
from aws_cdk import (
  core,
  aws_ec2 as ec2,
)

src_root_dir = os.path.join(os.path.dirname(__file__))

class LandingZone(ILandingZone):
  def __init__(self, scope:Construct, id:str, **kwargs)->None:
    super().__init__(scope, id, **kwargs)
    core.Tags.of(self).add('landing_zone', self.zone_name)
    
    self.backup_policy = BackupStrategyConstruct(self,'Backup', landing_zone=self)

  @property
  def zone_name(self)->str:
    raise NotImplementedError()

class ProducerLandingZone(LandingZone):
  def __init__(self, scope:core.Construct, id:str, **kwargs)->None:
    super().__init__(scope, id, **kwargs)

    self.storage = StorageConstruct(self,'Storage')

  @property
  def cidr_block(self)->str:
    raise NotImplementedError()

  @property
  def zone_name(self)->str:
    return 'Producer'

  @property
  def subnet_configuration(self)->List[ec2.SubnetConfiguration]:
    return [
      ec2.SubnetConfiguration(name='Public', subnet_type= ec2.SubnetType.PUBLIC, cidr_mask=24),
      ec2.SubnetConfiguration(name='Private', subnet_type= ec2.SubnetType.PRIVATE, cidr_mask=17),
    ]
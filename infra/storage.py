#!/usr/bin/env python3
import os.path
from typing import List
from infra.interfaces import ILandingZone
from aws_cdk import (
  core,
  aws_ec2 as ec2,
  aws_s3 as s3,
  aws_dynamodb as ddb,
)

class StorageConstruct(core.Construct):
  def __init__(self, scope:core.Construct, id:str, **kwargs)->None:
    super().__init__(scope, id, **kwargs)

    self.bucket = s3.Bucket(self,'Bucket',
      bucket_name='nbachmei.rekognition.{}'.format(core.Stack.of(self).region),
      removal_policy= core.RemovalPolicy.DESTROY,
      lifecycle_rules=[
        s3.LifecycleRule(
          abort_incomplete_multipart_upload_after=core.Duration.days(1),
          expiration= core.Duration.days(90))
      ])

    self.table = ddb.Table(self,'Experiments',
      table_name='Rekognition',
      partition_key= ddb.Attribute(
        name='PartitionKey',
        type = ddb.AttributeType.STRING),
      sort_key = ddb.Attribute(
        name='SortKey',
        type = ddb.AttributeType.STRING),
      billing_mode= ddb.BillingMode.PAY_PER_REQUEST,
      removal_policy = core.RemovalPolicy.DESTROY)

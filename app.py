#!/usr/bin/env python3
import os.path
from typing import List
from aws_cdk import core
from infra.basenet import Producer
from infra.landing_zone import ILandingZone

src_root_dir = os.path.join(os.path.dirname(__file__))

us_east_1 = core.Environment(region="us-east-1", account='581361757134')
eu_west_1 = core.Environment(region="eu-west-1", account='581361757134')
ap_ne_1 = core.Environment(region='ap-northeast-1', account='581361757134')
us_west_2 = core.Environment(region='us-west-2', account='581361757134')
ca_central_1 =core.Environment(region='ca-central-1', account='581361757134')

class NetworkingApp(core.App):
  def __init__(self, **kwargs) ->None:
    super().__init__(**kwargs)

    self.producer = Producer(self,'RekProducer', env=us_east_1)

  @property
  def zones(self)->List[ILandingZone]:
    return [ self.producer ]

app = NetworkingApp()
app.synth()

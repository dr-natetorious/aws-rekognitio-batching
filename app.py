#!/usr/bin/env python3
import os.path
from typing import List
from aws_cdk import core
from infra.interfaces import ILandingZone
from infra.landing_zone import ProducerLandingZone


src_root_dir = os.path.join(os.path.dirname(__file__))
us_west_2 = core.Environment(region="us-west-2", account='581361757134')

class NetworkingApp(core.App):
  def __init__(self, **kwargs) ->None:
    super().__init__(**kwargs)

    self.producer = ProducerLandingZone(self,'RekProducer', env=us_west_2)

  @property
  def zones(self)->List[ILandingZone]:
    return [ self.producer ]

app = NetworkingApp()
app.synth()

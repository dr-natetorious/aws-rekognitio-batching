import boto3
from os import path
from json import dumps
from labels import LabelDocument
rekognition = boto3.client('rekognition',region_name='us-west-2')

image_uri = 's3://nbachmei.rekognition.us-west-2/yelp/mGS7ZnsKPRxfB09fuRWnaw.jpg'
bucket = image_uri.split('/')[2]
key = '/'.join(image_uri.split('/')[3:])

response = rekognition.detect_labels(
  MaxLabels=1000,
  #MinConfidence=55,
  Image={
    'S3Object':{
      'Bucket': bucket,
      'Name': key
    },
  })

#print(dumps(response, indent=True))
document = LabelDocument(response)
names = ', '.join(sorted([x.name for x in document.bounded_labels]))
print(names)


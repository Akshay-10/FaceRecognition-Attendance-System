'''import boto3
import pandas as pd

s3=boto3.client("s3")
bucket_name="smartauthorizingsystem"
s3_object="photos/images/1.jpeg"
obj=s3.get_object(Bucket=bucket_name,key=s3_object)'''

import boto3
from io import BytesIO
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

resource = boto3.resource('s3', region_name='us-west-2')
bucket = resource.Bucket('smartauthorizingsystem')

image_object = bucket.Object('photos/images/101.jpeg')
image = mpimg.imread(BytesIO(image_object.get()['Body'].read()), 'jpeg')

plt.figure(0)
plt.imshow(image)
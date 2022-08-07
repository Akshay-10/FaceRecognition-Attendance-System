import boto3
import os
from botocore.exceptions import ClientError

Access_key_ID='AKIA3YJBIIAFWG56AJPE'
Secret_access_key='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'
bucket_name='smartauthorizingsys'
client_s3=boto3.client('s3',aws_access_key_id=Access_key_ID,aws_secret_access_key=Secret_access_key)

try:
    client_s3.upload_file('C:/Users/HP/PycharmProjects/FontendProjectH/entry/07_08_2022.csv','smartauthorizingsys','07_08_2022.csv')
except ClientError as e:
    print(e)
except Exception as e:
    print(e)

'''client_s3.delete_object(Bucket=bucket_name,Key='07_08_2022.csv')'''
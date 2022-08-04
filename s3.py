import boto3

s3 = boto3.client("s3")
s3.upload_file('C:/Users/HP/Pictures/attnsscreen.png','smartauthorizingsystem','attnsscreen.png')
'''s3_object="photos/images/1.jpeg"
obj=s3.get_object(Bucket=bucket_name,key=s3_object)'''
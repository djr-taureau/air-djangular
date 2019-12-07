import boto3
import uuid
import json
import os
from boto3.s3.transfer import TransferConfig
# from progress_percentage import ProgressPercentage

# conn = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
# s3_connection = s3_resource.meta.client
# s3_resource.meta.client.generate_preassigned_url()


def create_bucket_name(bucket_prefix):
    return ''.join([bucket_prefix, str(uuid.uuid4())])


def create_bucket(bucket_prefix, s3_connection):
    session = boto3.session.Session()
    current_region = session.region_name
    bucket_name = create_bucket_name(bucket_prefix)
    bucket_response = s3_connection.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': current_region
        }
    )
    print(bucket_name, current_region)
    # print(bucket_response)
    return bucket_name, bucket_response


def list_buckets():
    return s3_client.list_buckets()


def create_temp_file(size, file_name, file_content):
    random_file_name = ''.join([str(uuid.uuid4().hex[:6]), file_name])
    with open(random_file_name, 'w') as f:
        f.write(str(file_content) * size)
    return random_file_name


# first_file_name = create_temp_file(300, 'firstfile.txt', 'f')
# bucket_name, bucket_response = create_bucket(bucket_prefix='djr-taureau-bucket',
#                                              s3_connection=s3_resource.meta.client)

# first_file_name = create_temp_file(300, 'firstfile.txt', 'f')

# main_bucket = s3_resource.Bucket(name=bucket_name)
# main_object = s3_resource.Object(
#     bucket_name=main_bucket, key=first_file_name)

# print(bucket_name)
# print(bucket_response)
# print(main_bucket)
# print(main_object)
print(list_buckets())

import logging
import boto3
from botocore.exceptions import ClientError
import os
import pickle 

# bucket = 'cloud-computing.s3.ir-thr-at1.arvanstorage.com'
bucket = 'cloud-computing'

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3',
        endpoint_url='https://s3.ir-thr-at1.arvanstorage.com',
        aws_access_key_id='8b7c6be9-339e-4484-bd62-b068a696e348',
        aws_secret_access_key='72e62119eaf43dfeb321871d413f9646f39e35f1')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

upload_file(file_name='1.jpg', bucket=bucket)
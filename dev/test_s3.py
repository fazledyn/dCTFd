import boto3
from botocore.client import Config

AWS_ACCESS_KEY_ID     = ""
AWS_SECRET_ACCESS_KEY = ""
AWS_S3_BUCKET         = ""
AWS_S3_ENDPOINT_URL   = ""
AWS_S3_REGION         = ""

client = boto3.client(
    service_name="s3",
    config=Config(signature_version="s3v4"),
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    endpoint_url=AWS_S3_ENDPOINT_URL,
    region_name=AWS_S3_REGION,
)

res = boto3.resource(
    service_name="s3",
    config=Config(signature_version="s3v4"),
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    endpoint_url=AWS_S3_ENDPOINT_URL,
    region_name=AWS_S3_REGION,
)

print('Buckets:\n\t', *[b.name for b in res.buckets.all()], sep="\n\t")
print(client)
print(res)


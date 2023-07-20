import boto3

from botocore.client import Config

AWS_ACCESS_KEY_ID     = "DO00UKLYWFFQ9DW7XZBJ"
AWS_SECRET_ACCESS_KEY = "r8kPYjNkntJnxGD+QQaxGf7gQBWadZ7I219dBrlVx4Q"
AWS_S3_BUCKET         = "bcf23-final"
AWS_S3_ENDPOINT_URL   = "https://sgp1.digitaloceanspaces.com"
AWS_S3_REGION         = "sgp1"



client = boto3.client(
    service_name="s3",
    # config=Config(signature_version="s3v4"),
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





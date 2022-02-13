import boto3

session = boto3.session.Session()
client = session.client('s3',
                        region_name='nyc3',
                        endpoint_url='httpsnyc3.digitaloceanspaces.com',
                        aws_access_key_id='aws_access_key_id',
                        aws_secret_access_key='aws_secret_access_key')


resp = client.list_objects(Bucket='bucket', Prefix='image-path')

for obj in resp['Contents']:
    print(obj['Key'])

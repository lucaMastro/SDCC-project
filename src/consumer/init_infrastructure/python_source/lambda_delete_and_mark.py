import boto3 

from variables import MESSAGE_BUCKET_NAME

def delete_and_mark(event, context):
    client = boto3.client('s3')
    for key in event:
        if event[key] == 'mark':
            client.put_object_tagging(Bucket = MESSAGE_BUCKET_NAME, Key = key,
                Tagging={
                    'TagSet': [
                        {
                            'Key': 'new',
                            'Value': 'False'
                        }]
                })
        else:
            client.delete_object(Bucket=MESSAGE_BUCKET_NAME, Key=key)

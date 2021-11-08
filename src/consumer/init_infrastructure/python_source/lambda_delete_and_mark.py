import boto3 
#---------------------------------------------
from variables import MESSAGE_BUCKET_NAME
#---------------------------------------------

def delete_and_mark(event, context):
    client = boto3.client('s3')
    for key in event:
        if event[key] == 'mark':
            # changing the tag value
            client.put_object_tagging(Bucket = MESSAGE_BUCKET_NAME, Key = key,
                Tagging={
                    'TagSet': [
                        {
                            'Key': 'new',
                            'Value': 'False'
                        }]
                })
        elif event[key] == 'del':
            # deleting object
            client.delete_object(Bucket=MESSAGE_BUCKET_NAME, Key=key)

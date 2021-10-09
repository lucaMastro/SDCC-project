import boto3 

MESSAGE_BUCKET_NAME = "message-bucket-sdcc-20-21"

def manage_del_and_mark(event, context):
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

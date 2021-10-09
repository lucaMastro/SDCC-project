import boto3 
import Message as msg 

MESSAGE_BUCKET_NAME = "message-bucket-sdcc-20-21"

def doesFolderExist(path):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(MESSAGE_BUCKET_NAME) 

    return sum(1 for _ in bucket.objects.filter(Prefix=path)) > 0


def send_message(event, context):
    response = []
    for record in event['Records']:

        body = record['body']
        sender = record['messageAttributes']['From']['stringValue']
        receivers = record['messageAttributes']['To']['stringValue']
        obj = record['messageAttributes']['Object']['stringValue']
        folder_name = record['messageAttributes']['Folder']['stringValue']

        client = boto3.client('s3')
        # checking if message is sent to an exist user. Only in this case
        # proceed, otherwise doesnt create message
        if doesFolderExist(folder_name):

            rec_msg = msg.Message(receivers, sender, obj, body)
            key = "{}/{}".format(folder_name, context.aws_request_id)

            data = str(rec_msg)
            # metadata added to identify new msgs
            # bucket.put(Body=data.encode('utf-8'), Metadata={'new': 'True'})
            tmp_resp = client.put_object(Bucket = MESSAGE_BUCKET_NAME, Key = key, Body=data)
            response.append(tmp_resp)
            tmp_response = client.put_object_tagging(
                Bucket = MESSAGE_BUCKET_NAME,
                Key = key,
                Tagging={
                    'TagSet': [
                        {
                            'Key': 'new',
                            'Value': 'True'
                        },
                    ]
                },
            )
            response.append(tmp_resp)


    return response

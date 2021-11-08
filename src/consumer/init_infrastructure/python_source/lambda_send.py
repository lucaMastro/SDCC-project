import boto3 
#---------------------------------------------
import Message as msg 
from variables import MESSAGE_BUCKET_NAME
#---------------------------------------------

def doesFolderExist(path):
    # check is the folder exists
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(MESSAGE_BUCKET_NAME) 

    return sum(1 for _ in bucket.objects.filter(Prefix=path)) > 0


def send_message(event, context):
    response = []
    # in the SQS there can be more than 1 SQS message.
    for record in event['Records']:
        # getting the folder where to store the message
        folder_name = record['messageAttributes']['Folder']['stringValue']

        # checking if message is sent to an exist user. Only in this case
        # proceed, otherwise dont create message
        if doesFolderExist(folder_name):

            # getting sqs body -> message text field
            body = record['body']
            # getting sqs message attributes -> other message fields
            sender = record['messageAttributes']['From']['stringValue']
            receivers = record['messageAttributes']['To']['stringValue']
            obj = record['messageAttributes']['Object']['stringValue']
            
            client = boto3.client('s3')
            # creating a Message object: it's easy to cast to string
            rec_msg = msg.Message(receivers, sender, obj, body)
            
            # creating the name of the s3 object that will represent the
            # message
            key = "{}/{}".format(folder_name, context.aws_request_id)

            # convert the message to string. It's possible because the Message
            # class defines the __str__() method.
            data = str(rec_msg)

            # store the message
            client.put_object(Bucket = MESSAGE_BUCKET_NAME, Key = key, Body=data)

            # tagging the object
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

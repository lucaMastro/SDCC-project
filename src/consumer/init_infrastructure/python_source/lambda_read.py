import boto3
from variables import MESSAGE_BUCKET_NAME

def doesFolderExist(path):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(MESSAGE_BUCKET_NAME) 

    return sum(1 for _ in bucket.objects.filter(Prefix=path)) > 0



def read_messages(event, context):
    readAllMessages = event['All']
    user = event['Username']
        
    client = boto3.client('s3')
    
    # making folder name
    folder = '{}/'.format(user)
    messages = []
    newMessages = []
    
    response = client.list_objects_v2(Bucket=MESSAGE_BUCKET_NAME, Prefix=folder)
    # response is a dic. there is the pair 'Contents' : list. the list keeps the objects entry.
    listOfObjects = response['Contents']

    #sorting list
    get_last_modified = lambda obj: int(obj['LastModified'].strftime('%s'))
    sortedListOfKeys = [obj['Key'] for obj in sorted(listOfObjects,
        key=get_last_modified, reverse = True)]
    
    # Each element of the list is a dict that keeps key and other data. We only need keys:
    listOfKeys = []
    for k in sortedListOfKeys:
        # resonse keeps also the folder key. just excluding it:
        if not k.endswith(folder):
            listOfKeys.append(k)
    
    # reading all messages. obj type is ObjectSummary
    output = {}
    index = 0
    for key in listOfKeys:
        fields = {}
        # getting tag of the object:
        response = client.get_object_tagging(Bucket = MESSAGE_BUCKET_NAME, Key = key)
        # look at doc for response format:  
        # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.get_object_tagging
        isNew = response['TagSet'][0]['Value']
        
        if readAllMessages or (not readAllMessages and isNew == 'True'):
        
            fields['new'] = isNew
            fields['key'] = key
            # reading the message:
            objContent = client.get_object(Bucket=MESSAGE_BUCKET_NAME, Key=key)['Body'].read().decode('utf-8')
            fields['message'] = objContent 
       
        
            output[str(index)] = fields
            index += 1
    return output

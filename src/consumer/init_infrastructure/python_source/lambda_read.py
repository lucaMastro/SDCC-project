import boto3
#---------------------------------------------
from variables import MESSAGE_BUCKET_NAME
#---------------------------------------------

def doesFolderExist(path):
    # this function is meant to check if a folder exists
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(MESSAGE_BUCKET_NAME) 

    return sum(1 for _ in bucket.objects.filter(Prefix=path)) > 0



def read_messages(event, context):
    # getting input params:
    #
    # this value define if the function has to retrieve all messages of the
    # user or only the not-read ones.
    readAllMessages = event['All']
    user = event['Username']
        
    client = boto3.client('s3')
    
    # making folder name
    folder = user + '/'
    
    # getting all the messages
    #
    response = client.list_objects_v2(Bucket=MESSAGE_BUCKET_NAME, Prefix=folder)
    # response is a dic. there is the pair 'Contents' : list. the list keeps the objects entry.
    listOfObjects = response['Contents']

    # sorting list by timestamp in reverse order: from the newest to the oldest
    # and getting only the key
    get_last_modified = lambda obj: int(obj['LastModified'].strftime('%s'))
    listOfKeys = [obj['Key'] for obj in sorted(listOfObjects,
        key=get_last_modified, reverse = True)]

    # there is an '<user>/' in the list: it's only the name of the folder.
    # removing it
    listOfKeys.remove(folder)
    
    # now we have the list of key sorted by timestamp. let's continue creating
    # an output dictionary with the following form:
    #   int : dict
    # the key is the position in the ordered list, the dict keeps information
    # for a single message.
    output = {}
    index = 0
    for key in listOfKeys:
        fields = {}
        # getting tag of the object:
        response = client.get_object_tagging(Bucket = MESSAGE_BUCKET_NAME, Key = key)
        # look at doc for response format:  
        # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.get_object_tagging
        isNew = response['TagSet'][0]['Value']
        
        # this check exclude the non-new messages when user wants to read only
        # the not-read ones
        if readAllMessages or (not readAllMessages and isNew == 'True'):
        
            fields['new'] = isNew
            fields['key'] = key
            # reading the message:
            objContent = client.get_object(Bucket=MESSAGE_BUCKET_NAME, Key=key)['Body'].read().decode('utf-8')
            fields['message'] = objContent 
       
            output[index] = fields
            index += 1

    return output

import boto3 
import mysql.connector 

import host as h
import Message as msg 

MESSAGE_BUCKET_NAME = "message-bucket-sdcc-20-21"

#---------------------------------------------
def connectToDb():
    
     return mysql.connector.connect(
        host=h.DB_HOST,
        database='users_db',
        user='admin',
        password='sdcc-db-admin')

#---------------------------------------------

def performeRegistration(usr, pw):
    conn = connectToDb()
    conn._open_connection()
    args = (usr, pw)
    cursor = conn.cursor()
    
    try:
        cursor.callproc("sign_in", args)
        a = True
    except Exception as e:
        a = False
        # for logging 
        print('The exception is: ', str(e))
    finally:
        conn.close()

    # create a folder for the user:
    s3 = boto3.client('s3')
    bucket_name = MESSAGE_BUCKET_NAME 
    folder_name = usr 
    s3.put_object(Bucket=bucket_name, Key=(folder_name+'/'))

    return a
    
def performeLogin(usr, pw):
    conn = connectToDb()
    conn._open_connection()
    
    args = (usr, pw)
    cursor = conn.cursor()
    try:
        cursor.callproc("log_in", args)
        a = True
    except Exception as e:
        a = False
        # for logging 
        print('The exception is: ', str(e))
    finally:
        conn.close()
    return a

def sign_in_log_in(event, context):
    operation = event['Operation']

    usr = event['Username']
    pw = event['Password']

    if operation == 'Registration':
        a = performeRegistration(usr, pw)
    else:
        a = performeLogin(usr, pw)

    return a

#---------------------------------------------

def users_list(event, context):
    #TODO
    conn = connectToDb()
    conn._open_connection()
    
    cursor = conn.cursor()
    try:
        cursor.callproc("get_user_list")
        l = []
        for result in cursor.stored_results():
            tmp = result.fetchall()
            for usr in tmp:
                l.append(usr[0])

    except Exception as e:
        l = None
        # for logging 
        print('The exception is: ', str(e))
    finally:
        conn.close()
    return l

#---------------------------------------------

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
    
    # Each element of the list is a dict that keeps key and other data. We only need keys:
    listOfKeys = []
    for obj in listOfObjects:
        k = obj['Key']
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
#---------------------------------------------

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




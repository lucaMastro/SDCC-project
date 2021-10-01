import boto3 
import mysql.connector 

import host as h
import Message as msg 

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
    bucket_name = "message-bucket-sdcc-20-21"
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

def read_messages(event, context):
    #TODO
    return 0

#---------------------------------------------

def send_message(event, context):
    for record in event['Records']:

        body = record['body']
        sender = record['messageAttributes']['From']['stringValue']
        receivers = record['messageAttributes']['To']['stringValue']
        obj = record['messageAttributes']['Object']['stringValue']
        folder_name = record['messageAttributes']['Folder']['stringValue']
        rec_msg = msg.Message(receivers, sender, obj, body)
        
        key = "{}/{}".format(folder_name, context.aws_request_id)
        print('key = ', key)
        s3 = boto3.resource('s3')
        bucket = s3.Object('message-bucket-sdcc-20-21', key) 
        data = str(rec_msg)
        # metadata added to identify new msgs
        bucket.put(Body=data.encode('utf-8'), Metadata={'new': 'True'})

    return True

#---------------------------------------------


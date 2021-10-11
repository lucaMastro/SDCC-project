import boto3 
import mysql.connector 

import host as h

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
        a = str(e) 
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

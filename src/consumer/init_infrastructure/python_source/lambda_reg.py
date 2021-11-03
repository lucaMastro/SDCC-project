import boto3 
import mysql.connector 
import os
import string
import hmac
import hashlib

MESSAGE_BUCKET_NAME = "message-bucket-sdcc-20-21"

#---------------------------------------------
def connectToDb():
    
    client = boto3.client('rds')
    db_identifier = 'sdcc-rds'
    response = client.describe_db_instances()
    host =  response['DBInstances'][0]['Endpoint']['Address']

    return mysql.connector.connect(
        host=host,
        database='users_db',
        user='admin',
        password='sdcc-db-admin')

def genSalt():
    # 64 elements string
    chars = string.ascii_uppercase + string.digits + string.ascii_lowercase + '+' + '-'
    
    salt = ''
    for i in range(32): # 256 bits
        index = ord(os.urandom(1)) % 64
        salt += chars[index]

    return salt

def encrypt(pw, salt):
    h = hmac.new(str.encode(pw), str.encode(salt), hashlib.sha256)
    return h.hexdigest() 

#---------------------------------------------

def performeRegistration(usr, pw):
    conn = connectToDb()
    conn._open_connection()
    cursor = conn.cursor()
    
    # genereting salt
    salt = genSalt()
    # encrypt the pw
    pw = encrypt(pw, salt)

    try:
        args = (usr, pw, salt)
        cursor.callproc("sign_up", args)
        a = True
    except Exception as e:
        a = str(e) 
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
    
    cursor = conn.cursor()
    try:
        #getting pw form db:
        args = (usr, '')
        ret = cursor.callproc("get_salt", args)
        salt = ret[1]
        # encrypt pw:
        pw = encrypt(pw, salt)

        args = (usr, pw)
        cursor.callproc("log_in", args)
        a = True
    except Exception as e:
        a = str(e) 
        # for logging 
        print('The exception is: ', str(e))
    finally:
        conn.close()
    return a

def sign_up_log_in(event, context):
    operation = event['Operation']

    usr = event['Username']
    pw = event['Password']

    if operation == 'Registration':
        a = performeRegistration(usr, pw)
    else:
        a = performeLogin(usr, pw)

    return a

#---------------------------------------------

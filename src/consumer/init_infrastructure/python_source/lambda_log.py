import boto3 
#---------------------------------------------
import db_helper as helper 
from variables import MESSAGE_BUCKET_NAME
#---------------------------------------------

def log_in(event, context):
    # getting input params
    usr = event['Username']
    pw = event['Password']

    # create connection and open it
    conn = helper.connectToDb()
    conn._open_connection()
    
    cursor = conn.cursor()
    try:
        # getting pw form db:
        args = (usr, '')
        ret = cursor.callproc("get_salt", args)
        salt = ret[1] # it's an out param of procedure
        # encrypt input pw:
        pw = helper.encrypt(pw, salt)
        
        # check for login
        args = (usr, pw)
        cursor.callproc("log_in", args)
        ret = True
    except Exception as e:
        ret = str(e) 
        # for logging 
        print('The exception is: ', str(e))
    finally:
        conn.close()
    return ret

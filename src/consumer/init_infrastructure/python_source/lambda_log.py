import boto3 
import db_helper as helper 


from variables import MESSAGE_BUCKET_NAME

def log_in(event, context):
    usr = event['Username']
    pw = event['Password']

    conn = helper.connectToDb()
    conn._open_connection()
    
    cursor = conn.cursor()
    try:
        #getting pw form db:
        args = (usr, '')
        ret = cursor.callproc("get_salt", args)
        salt = ret[1]
        # encrypt pw:
        pw = helper.encrypt(pw, salt)

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


#---------------------------------------------

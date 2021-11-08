import boto3 
#---------------------------------------------
import db_helper as helper 
from variables import MESSAGE_BUCKET_NAME
#---------------------------------------------

    
def sign_up(event, context):
    # getting input params
    usr = event['Username']
    pw = event['Password']

    # open connection to rds db
    conn = helper.connectToDb()
    conn._open_connection()
    cursor = conn.cursor()
    
    # genereting salt
    salt = helper.genSalt()
    # encrypt the pw
    pw = helper.encrypt(pw, salt)

    try:
        # calling the sign up stored procedure
        args = (usr, pw, salt)
        cursor.callproc("sign_up", args)
        ret = True
    except Exception as e:
        ret = str(e) 
        # for logging 
        print('The exception is: ', str(e))
    finally:
        conn.close()

    # create a folder for the user:
    s3 = boto3.client('s3')
    bucket_name = MESSAGE_BUCKET_NAME 
    folder_name = usr + '/'
    s3.put_object(Bucket=bucket_name, Key=folder_name)

    return ret

import boto3 
import db_helper as helper 

MESSAGE_BUCKET_NAME = "message-bucket-sdcc-20-21"


#---------------------------------------------

    
def sign_up(event, context):
    usr = event['Username']
    pw = event['Password']

    conn = helper.connectToDb()
    conn._open_connection()
    cursor = conn.cursor()
    
    # genereting salt
    salt = helper.genSalt()
    # encrypt the pw
    pw = helper.encrypt(pw, salt)

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


#---------------------------------------------

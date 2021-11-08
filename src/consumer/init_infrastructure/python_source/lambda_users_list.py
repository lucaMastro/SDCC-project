import boto3 
import mysql.connector 
#---------------------------------------------
from db_helper import connectToDb
#---------------------------------------------


def users_list(event, context):
    # opening connection to rds db
    conn = connectToDb()
    conn._open_connection()

    cursor = conn.cursor()
    try:
        # calling store procedure
        cursor.callproc("get_user_list")

        # creating the list
        l = []
        for result in cursor.stored_results():
            tmp = result.fetchall()
            for usr in tmp:
                l.append(usr[0])

    except Exception as e:
        l = str(e)
        # for logging 
        print('The exception is: ', str(e))
    finally:
        conn.close()
    return l


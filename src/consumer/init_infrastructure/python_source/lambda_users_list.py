import boto3 
import mysql.connector 

from db_helper import connectToDb


def users_list(event, context):
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


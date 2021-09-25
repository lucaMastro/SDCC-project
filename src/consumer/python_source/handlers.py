import boto3 
import mysql.connector 

import host as h

#---------------------------------------------
def connectToDb():
    
     return mysql.connector.connect(
        host=h.DB_HOST,
        database='users_db',
        user='admin',
        password='sdcc-db-admin')


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
    return a
    

def performeLogin(usr, pw):
    #TODO
    return 

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

def users_list():
    #TODO
    return 0

def read_messages():
    #TODO
    return 0

def send_message():
    #TODO
    return 0



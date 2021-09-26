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

def read_messages():
    #TODO
    return 0

def send_message():
    #TODO
    return 0



import os
import string
import hmac
import hashlib
import mysql.connector 
import boto3 
import variables

def connectToDb():
    
    client = boto3.client('rds')
    db_identifier = variables.db_identifier  
    response = client.describe_db_instances()
    host =  response['DBInstances'][0]['Endpoint']['Address']

    return mysql.connector.connect(
        host=host,
        database=variables.database,
        user=variables.user,
        password=variables.password)

def encrypt(pw, salt):
    h = hmac.new(str.encode(pw), str.encode(salt), hashlib.sha256)
    return h.hexdigest() 

def genSalt():
    # 64 elements string
    chars = string.ascii_uppercase + string.digits + string.ascii_lowercase + '+' + '-'
    
    salt = ''
    for i in range(32): # 256 bits
        index = ord(os.urandom(1)) % 64
        salt += chars[index]

    return salt


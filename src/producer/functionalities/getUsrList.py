from getpass import getpass 
import boto3 
import json

def getUsrList():

    client = boto3.client('lambda')
    response = client.invoke( FunctionName='users_list',
            InvocationType='RequestResponse',
            LogType='Tail',
            Payload=json.dumps({}), )

    payload = response['Payload'].read().decode('utf-8')

    return payload


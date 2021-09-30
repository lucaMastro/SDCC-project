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

    # payload is a string: '["usr1", "usr2"...]'
    # converting it in a list:
    return convertToList(payload)


def convertToList(payload):
    # removing '[' and ']':
    s = payload[1:len(payload) - 1]

    # s now is '"a", "b"'. splitting it with, ','
    tmp = s.split(',')

    # tmp now is ['"a"', '" "', '"b"']. for each element, should remove the
    # double-quotes:
    l = []
    for item in tmp:
        l += item.split('"')
    
    # in l list, there are empty strings or one char string " ". removing them:
    for item in l:
        if item == '' or item == ' ':
            l.remove(item)

    return l
    


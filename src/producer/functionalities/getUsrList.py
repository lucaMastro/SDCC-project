import boto3 
import json
#---------------------------------------------

def getUsrList():

    client = boto3.client('lambda')
    response = client.invoke( FunctionName='users_list',
            InvocationType='RequestResponse',
            LogType='Tail',
            Payload=json.dumps({}), )

    payload = response['Payload'].read().decode('utf-8')

    # payload is a string: '["usr1", "usr2"...]'
    # converting it in a list:
    l = payload.strip('][').split(', ')
    res = []
    for i in l:
        # removing " from user_names: the l list is now:
        # ['"usr1"', '"usr2"' ...]
        res.append(i.strip('"'))
    return res

from stdiomask import getpass 
import boto3 
import json

# same function to perform registration and login: getting username and
# password and modify input value to specify if it's a registration or a login
# operation. The user param is None in graphic client, otherwise it's given at
# function invocation

def registrationLogin(operationCode, user=None, pw=None):
    input_params = {}

    # user == None never happends
    #if (user == None):
    #    user = input("Give me the username: ")
    if (pw == None):
        pw = getpass("Give me the password: ", mask='*')
    
    if operationCode == 1:
        operation = 'Registration'
    elif operationCode == 2:
        operation = 'Login'

    print('{}.'.format(pw))
    input()
    input_params = {}
    input_params['Operation'] = operation 
    input_params['Username'] = user 
    input_params['Password'] = pw  
    
    client = boto3.client('lambda')
    response = client.invoke( FunctionName='sign_log_in',
            InvocationType='RequestResponse',
            LogType='Tail',
            Payload=json.dumps(input_params), )

    payload = response['Payload'].read().decode('utf-8')

    return payload


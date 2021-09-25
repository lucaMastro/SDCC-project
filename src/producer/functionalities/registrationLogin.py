from getpass import getpass 
import boto3 
import json

# same function to perform registration and login: getting username and
# password and modify input value to specify if it's a registration or a login
# operation

def registrationLogin(operationCode):
    input_params = {}

    user = input("Give me the username: ")
    pw = getpass("Give me the password: ")
    
    if operationCode == 1:
        operation = 'Registration'
    if operationCode == 2:
        operation = 'Login'

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
    print(payload)
    return payload


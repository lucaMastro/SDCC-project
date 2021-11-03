from stdiomask import getpass 
import boto3 
import json

# same function to perform registration and login: getting username and
# password and modify input value to specify if it's a registration or a login
# operation. The user param is None in graphic client, otherwise it's given at
# function invocation

def genSalt(user):
    #TODO
    return 'ab'

def retrieveSalt(user):
    #TODO
    dic = dict()
    dic['salt'] = 'ab'
    return dic

def crypt(pw, salt):
    #TODO
    return pw 

def registrationLogin(operationCode, user=None, pw=None):
    input_params = {}

    # user == None never happends
    #if (user == None):
    #    user = input("Give me the username: ")
    if (pw == None):
        pw = getpass("Give me the password: ", mask='*')
    
    if operationCode == 1:
        fun_name = 'sign_up'

    elif operationCode == 2:
        fun_name = 'log_in'

    # encryption of pw is done by the lambda function which is addicted to
    # the registration. This is not a problem because the communication is
    # based on TLS. We need encryption because we don't wanto to store pw
    # in clear in db.
    input_params = {}
    input_params['Username'] = user 
    input_params['Password'] = pw  
    
    client = boto3.client('lambda')
    response = client.invoke( FunctionName=fun_name,
            InvocationType='RequestResponse',
            LogType='Tail',
            Payload=json.dumps(input_params), )

    payload = response['Payload'].read().decode('utf-8')

    return payload


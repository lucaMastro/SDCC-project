import boto3

def getMessages(All = True):
    
    sqs = boto3.resource('lambda')
    #next dict can be passed as parament already filled
    #input_params = {}
    #input_params['all'] = True
    #input_params['username'] = username
    response = client.invoke( FunctionName='read_messages',
            InvocationType='RequestResponse',
            LogType='Tail',
            Payload=json.dumps(input_params), )

    #TODO
    returned = queue.sendMessage(body='')

    print(returned)


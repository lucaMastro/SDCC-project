import boto3
import json

def manageDelAndMark(inputDict):
    client = boto3.client('lambda')
    response = client.invoke( FunctionName='delete_and_mark',
                InvocationType='RequestResponse',
                LogType='Tail',
                Payload=json.dumps(inputDict))
    

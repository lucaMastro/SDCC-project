import boto3

def getUsrList():
    
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName='usr_list_sqs_queue')

    returned = queue.sendMessage(body='')

    print(returned)


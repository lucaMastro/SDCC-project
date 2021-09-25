import boto3

def getMessages(All = True):
    
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName='read_messages_sqs_queue')

    #TODO
    returned = queue.sendMessage(body='')

    print(returned)


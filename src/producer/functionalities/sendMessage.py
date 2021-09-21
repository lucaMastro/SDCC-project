import boto3 
#from Message import Message

def getReceiversList():
    rec_list = []

    other_user = True
    while other_user:
        receiver = input("give me a receiver: ")
        rec_list.append(receiver)
        
        # ask for another user
        valid_answer = False
        while not valid_answer:
            tmp = inpu("do you want to add another receiver? (yes, no)")
            if (tmp == 'yes'):
                valid_answer = True 
                print()
        
            else if (tmp == 'no'):
                valid_answer = True 
                other_user = False

            else:
                print('answr not valid. Retry:')

    return rec_list 

        

def sendMessage(sender):
    receivers = getReceiversList() 
    object_ = input("Give me the object: ")
    text = input("Give me the text: ")

    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName='send_message_sqs_queue')

    for rec in receivers:
        queue.send_message(MessageBody = text, Attributes = {
            'From' : {
                'StringValue' : sender,
                'DataType' : 'String'
                },
            'To' : {
                'StringValue' : rec,
                'DataType' : 'String'
                },
            'Object' : {
                'StringValue' : sender,
                'DataType' : 'String'
                }
            })

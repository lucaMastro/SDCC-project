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
            tmp = input("do you want to add another receiver? (yes, no)")
            if (tmp == 'yes'):
                valid_answer = True 
                print()
        
            elif (tmp == 'no'):
                valid_answer = True 
                other_user = False

            else:
                print('answr not valid. Retry:')

    return rec_list 


def getMsgBody():
    lines = ''
    while True:
        l = input()
        if l == '':
            break
        else:
            lines += l + '\n'

    print('\nSending message(s)...')
    return lines 


        
def sendMessage(sender, receivers = None):
    # usr list not None when called by Cli client
    if receivers == None:
        receivers = getReceiversList() 
    object_ = input("Give me the object: ")
    print('Give me message text (to stop input, insert a blank line):')
    text = getMsgBody() 

    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName='send_messages_sqs_queue')

    for rec in receivers:
        queue.send_message(MessageBody = text, MessageAttributes = {
            'From' : {
                'StringValue' : sender,
                'DataType' : 'String'
                },
            'To' : {
                'StringValue' : rec,
                'DataType' : 'String'
                },
            'Object' : {
                'StringValue' : object_,
                'DataType' : 'String'
                }
            })

    print("Message(s) sent")

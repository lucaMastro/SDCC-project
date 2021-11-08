import boto3 
#---------------------------------------------

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

def makeStringFromList(l):
    # ['a', 'b', 'c'] -> 'a, b, c'
    s = ''
    for i in range(len(l) - 1):
      s += l[i] + ', '
    s += l[len(l) - 1]
    return s
  
        
def sendMessage(params):
    object_ = params['object']
    receivers = params['receivers'] #this is a list of string
    sender = params['sender']

    # convert the list into a string: it will be the "To" message attribute of
    # SQS message and, if it's a reply use case, it will be printed
    str_list = makeStringFromList(receivers) 
    if params['reply']:
        print('to: {}'.format(str_list))
        print('object: {}'.format(object_))

    text = params['body']
    if text == None: # cli-case
        print('Give me message text (to stop input, insert a blank line):')
        text = getMsgBody() 
        
    # message SQS body cannot be an empty string
    if text == '':
        text = ' '

    # getting sqs queue
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName='send_messages_sqs_queue')

    # for each receiver send a copy of the message
    for rec in receivers:
        queue.send_message(MessageBody = text, MessageAttributes = {
            # attributes for Message() fields
            'From' : {
                'StringValue' : sender,
                'DataType' : 'String'
                },
            'To' : {
                'StringValue' : str_list, #all the listed users
                'DataType' : 'String'
                },
            'Object' : {
                'StringValue' : object_,
                'DataType' : 'String'
                },
            'Folder' : {
                'StringValue' : rec, #current receiver
                'DataType' : 'String'
                }
            })
    print('Message(s) sent.\n')


import boto3 


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
    s = ''
    for i in range(len(l) - 1):
      s += l[i] + ', '
    s += l[len(l) - 1]
    return s
  
        
def sendMessage(params):
    object_ = params['object']
    receivers = params['receivers']
    sender = params['sender']

    str_list = ''
    if params['reply']:
        str_list = makeStringFromList(receivers)
        print('to: {}'.format(str_list))
        print('object: {}'.format(object_))

    text = params['body']
    if text == None: # cli-case
        print('Give me message text (to stop input, insert a blank line):')
        text = getMsgBody() 
        
    if text == '':
        text = ' '

    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName='send_messages_sqs_queue')

    if str_list == '':
        str_list = makeStringFromList(receivers)    

    for rec in receivers:
        queue.send_message(MessageBody = text, MessageAttributes = {
            # attributes for Message() fields
            'From' : {
                'StringValue' : sender,
                'DataType' : 'String'
                },
            'To' : {
                'StringValue' : str_list,
                'DataType' : 'String'
                },
            'Object' : {
                'StringValue' : object_,
                'DataType' : 'String'
                },
            # folder name:
            'Folder' : {
                'StringValue' : rec,
                'DataType' : 'String'
                }
            })
    print('Message(s) sent.\n')


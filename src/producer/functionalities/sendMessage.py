import boto3 
#from Message import Message


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


        
def sendMessage(params):
    text = params['body']
    if text == None: # cli-case
        print('Give me message text (to stop input, insert a blank line):')
        text = getMsgBody() 
    object_ = params['object']
    receivers = params['receivers']
    sender = params['sender']
        
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName='send_messages_sqs_queue')

    str_list = ''
    for rec in receivers:
        str_list += rec + ', '
    # str_list is "a, b, c, ". removing last space and comma:
    str_list = str_list[:-2]

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

if __name__ == '__main__':
    p = {}
    p['receivers'] = ['luca', 'asd']
    p['object'] = 'prova' 
    p['body'] = 'test' 
    p['sender'] = 'luca'

    sendMessage(p)

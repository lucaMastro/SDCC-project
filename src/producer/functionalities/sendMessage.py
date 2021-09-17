from Message import Message

def sendMessage(sender):
    receiver = input("Give me the receiver: ")
    object_ = input("Give me the object: ")
    text = input("Give me the text: ")

    mess = Message(receiver, sender, object_, text)

    print(str(mess))


    

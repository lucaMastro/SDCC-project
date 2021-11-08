class Message:

    #e-mail constructor
    def __init__(self, *args):
        if len(args) > 1:
            to = args[0] 
            from_ = args[1]
            object_ = args[2]
            text = args[3]
        else:
            # create message from its string representation
            string = args[0]

            l = string.split('\n')
            from_ = l[0][6:]
            to = l[1][4:]
            object_ = l[2][8:]
            text = l[3][6:]
            for i in range(4, len(l)):
                if l[i] != '':
                    text += '\n' + l[i]
        self.to = to
        self.from_ = from_
        self.object_ = object_
        self.text = text

    def __str__(self):
        #just return the string which represents the object

        message = "From: " + self.from_ + "\nTo: " + self.to + "\nObject: " + self.object_ + "\nBody: " + self.text + "\n"
        return message

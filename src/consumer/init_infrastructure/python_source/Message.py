"""
This code is the python class that will be used to represent message
"""


class Message:

    #e-mail constructor
    def __init__(self, to, from_, object_, text):
        self.to = to
        self.from_ = from_
        self.object_ = object_
        self.text = text

    def __str__(self):
        #just return the string which represents the object

        email = "From: " + self.from_ + "\nTo: " + self.to + "\nObject: " + self.object_ + "\nBody: " + self.text + "\n"
        return email

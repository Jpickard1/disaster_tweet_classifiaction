import re

class Ctweet:

    def __init__(self):
        self.setId(1)
        self.setKeyword("string")
        self.setLocation("string")
        self.setText("string")
        self.setTarget(1)

    def __str__(self):
        space = ' '
        message = space.join(self.getText())
        return self.getId() + ", " + self.getKeyword() + ", " + self.getLocation() + ", " + message + ", " + str(self.getTarget())

    def __repr__(self):
        space = ' '
        message = space.join(self.getText())
        return self.getId() + ", " + self.getKeyword() + ", " + self.getLocation() + ", " + message + ", " + str(self.getTarget())

    def getId(self):
        return self.id
    
    def setId(self, p_id):
        self.id = p_id

    def getKeyword(self):
        return self.keyword
    
    def setKeyword(self, p_keyword):
        self.keyword = p_keyword

    def getLocation(self):
        return self.location
    
    def setLocation(self, p_location):
        self.location = p_location

    def getText(self):
        return self.text

    ###################################################################
    #
    #   1. removes all nonalphanumeric characters from text
    #   2. sets all links to the string literal defined below
    #
    ###################################################################    
    def formatWord(self, word):
        if len(word) > 4 and word[0:4] == "http":
            return "1234http5678link"
        else:
            return re.sub('[\W_]', '', word)

    def setText(self, p_text):
        self.text =p_text.lower().split()
        i = 0
        while i < len(self.text):
            formated_word = self.formatWord(self.text[i])
            self.text[i] = formated_word
            i = i + 1

    def getTarget(self):
        return self.target
    
    def setTarget(self, p_target):
        if p_target == "0" or p_target == "1":
            self.target = p_target
        else:
            self.target = -1

    def validate(self):
        if isinstance(self.getId(), int):
            return True
        else:
            return False

# END tweet class definition


import re

class tweet:

    def __init__(self):
        self.setId(1)
        self.setKeyword("string")
        self.setLocation("string")
        self.setText("string")
        self.setTarget(1)

    def __str__(self):
        space = ' '
        message = space.join(self.getText())
        return self.getId() + ", " + self.getKeyword() + ", " + self.getLocation() + ", " + message + ", " + self.getTarget()

    def __repr__(self):
        space = ' '
        message = space.join(self.getText())
        return self.getId() + ", " + self.getKeyword() + ", " + self.getLocation() + ", " + message + ", " + self.getTarget()

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
    
    def setText(self, p_text):
        self.text = p_text.lower().split()
        for word in self.text:
            if not link(word):
                word = re.sub('[\W_]+', '', word)
        # self.text = re.sub('[\W_]+', ' ', p_text).lower().split()

    def getTarget(self):
        return self.target
    
    def setTarget(self, p_target):
        self.target = p_target

    def validate(self):
        if isinstance(self.getId(), int):
            return True
        else:
            return False

# END tweet class definition

def link(word):
    if len(word) > 4 and word[0:4] == "http":
        return True
    else:
        return False


#########################################################################################
#
#                                       Tweet Class
#   Joshua Pickard                                                          June 2020
#   jpic@umich.edu
#
#   Purpose: Stores data read in from training and test CSV files
#
#   Class attributes:
#       1. id.........number associated with each tweet and line in the CSV files
#       2. keyword....data field from CSV
#       3. location...data field from CSV
#       4. text.......the message from the tweet is stored as a string
#       5. target.....if the text is about a disaster, then the target is 1. Otherwise,
#                     if it is labeled the target is 0. All nonevalutated or prelabeled
#                     tweets have a target of -1
#
#   Methods:
#       - getters and setters for all class attributes
#       - default constructor...
#       - printers..............
#       - formatWord............removes nonalphanumeric characters and changes all links
#                               to "1234http5678link"
#       - validate..............currently this is not helpful
#
#########################################################################################

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

    def setText(self, p_text):
        self.text =p_text

    def getTarget(self):
        return self.target
    
    def setTarget(self, p_target):
        self.target = p_target

    def validate(self):
        return True
        """
        if isinstance(self.getId(), int):
            return True
        else:
            return False"""

# END Ctweet class definition
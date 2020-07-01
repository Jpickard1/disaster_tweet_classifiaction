#########################################################################################
#
#                                    Data Cleaner Class
#   Joshua Pickard                                                          June 2020
#   jpic@umich.edu
#
#   Purpose: read the CSV file into Ctweet objects and build a dictionary of words
#            and their occurences in each type of tweet
#
#   Class attributes:
#       1. message_list...a list of tweet objects, each read in from a file in the CSV
#       2. catagories.....a dictionary all targets which stores the number of occurences 
#                         of each target
#   
#   Methods:
#       - read_csv........reads in csv file building message_list
#       - getMessages.....returns message_list
#       - getCatagories...returns catagories
#
#########################################################################################

import csv
from tweet import Ctweet

# CSV Format: id,keyword,location,text,target

class Cdata_cleaner:

    #####################################################################################
    #
    #   Cdata_cleaner:read_csv
    #       This reads a .csv file and creates a Ctweet corresponding to each line in the
    #       file. All Ctweets are placed in self.message_list. As lines are read in,
    #       this method also counts the number of occurences of each category.
    #
    #       Note: this function is commonly used to reformat .csv files into the standard
    #       data fields used for the project: id,keyword,location,text,target
    #
    #####################################################################################
    def read_csv(self, p_file_path):

        with open(p_file_path) as csvfile:
    
            # Read in csv file
            readCSV = csv.reader(csvfile, delimiter=',')
    
            # Create set of tweets
            self.message_list = list()
            self.catagories = dict()
            for row in readCSV:
                tweet1 = Ctweet()
                tweet1.setId(row[0])
                tweet1.setKeyword(row[1])
                tweet1.setLocation(row[2])
                tweet1.setText(row[3])
                tweet1.setTarget(row[4])
                self.message_list.append(tweet1)
                if row[4] in self.catagories:
                    self.catagories[row[4]] = self.catagories[row[4]] + 1
                else:
                    self.catagories[row[4]] = 1
    #####################################################################################
    #
    #   Cdata_cleaner:getters
    #       getter methods for all message_list and categories
    #
    #####################################################################################
    def getCatagories(self):
        return self.catagories

    def getMessages(self):
        return self.message_list
    
    # END getter methods

# END Cdata_cleaner class definition
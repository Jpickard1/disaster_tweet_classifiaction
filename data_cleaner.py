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
#       1. tweet_list...a list of tweet objects, each read in from a file in the CSV
#       2. dictionary...a dictionary of all words found in the tweets. Each word is a key
#                       storing the occurences of each word in each type of tweet
#                       dictionary[word] = [regular, disaster]
#       3. disaster.....stores the number of disaster tweets
#       4. regular......stores the number of regular tweets
#   
#   Methods:
#       - read_csv...........reads in csv file building tweet_list
#       - build_dictionary...converts tweet_list to dictionary
#       - dictionary.........returns the dictionary
#       - disaster...........returns the number of disaster tweets
#       - regular............returns the number of regular tweets
#
#########################################################################################

import csv
from tweet import Ctweet

# CSV Format: id,keyword,location,text,target

class Cdata_cleaner:

    def read_csv(self, p_file_path):

        with open(p_file_path) as csvfile:
    
            # Read in csv file
            readCSV = csv.reader(csvfile, delimiter=',')
    
            # Create set of tweets
            first = True
            self.tweet_list = list()
            for row in readCSV:
                tweet1 = Ctweet()
                tweet1.setId(row[0])
                tweet1.setKeyword(row[1])
                tweet1.setLocation(row[2])
                tweet1.setText(row[3])
                tweet1.setTarget(row[4])
                if first:
                    first = False
                else:
                    self.tweet_list.append(tweet1)
            return self.tweet_list
    
    def build_dictionary(self):
        self.dictionary = dict()
        for tweet1 in self.tweet_list:
            for word in tweet1.getText():
                index = int(tweet1.getTarget())
                if index >= 0:
                    if index == 0:
                        self.regular = self.regular + 1
                    else:
                        self.disaster = self.disaster + 1
                    if word not in self.dictionary:
                        self.dictionary[word] = [0,0]
                    self.dictionary.get(word)[index] = self.dictionary.get(word)[index] + 1
        ret = self.dictionary
        return ret

    def dictionary(self):
        return self.dictionary
    
    def disaster_number():
        return self.disaster

    def regular_number():
        return self.regular

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
                    if word not in self.dictionary:
                        self.dictionary[word] = [0,0]
                    self.dictionary.get(word)[index] = self.dictionary.get(word)[index] + 1
        ret = self.dictionary
        return ret

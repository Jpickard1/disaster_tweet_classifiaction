import sys
from naive_bayes_classifier import Cnaive_bayes
from data_cleaner import Cdata_cleaner
from tweet import Ctweet
"""
Cnaive_bayes classifier
training_set = "train.csv"
debug = True
classifier.train(training_set, debug)
test_set = "test.csv"
classifier.predict(test_set, debug)
"""

reader = Cdata_cleaner()
reader.read_csv("../../eecs280/p5/trainReddit.csv")
first = True
sys.stdout = open("trainReddit.csv", "w")
for message in reader.getMessages():
    if not first:
        print(",,,"+message.getKeyword()+","+str(message.getId()))
    if first:
        first = False


# GENERIC TEMPLATE

#########################################################################################
#
#                                    
#   Joshua Pickard                                                          June 2020
#   jpic@umich.edu
#
#   Purpose: 
#
#   Class attributes:
#       1.
#   
#   Methods:
#       -
#
#########################################################################################

"""

    cleaner = Cdata_cleaner()
    cleaner.read_csv('train.csv')
    dictionary = cleaner.build_dictionary()
    for word in dictionary:
        print(word + ": ")
        print(dictionary[word])

"""
import csv
from tweet import tweet
"""
with open('test.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:"""


with open('train.csv') as csvfile:
    
    # Read in csv file
    readCSV = csv.reader(csvfile, delimiter=',')
    
    # Create set of tweets
    tweet_list = []
    for row in readCSV:
        #print("loop")
        tweet1 = tweet()
        tweet1.setId(row[0])
        tweet1.setKeyword(row[1])
        tweet1.setLocation(row[2])
        tweet1.setText(row[3])
        tweet1.setTarget(row[4])
        #if tweet1.validate():
        tweet_list.append(tweet1)

    for tweet1 in tweet_list:
        print(tweet1)
    
    #print(tweet_list)
    # Build dictionary
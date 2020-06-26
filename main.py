from data_cleaner import Cdata_cleaner
from tweet import Ctweet

cleaner = Cdata_cleaner()
cleaner.read_csv('train.csv')
dictionary = cleaner.build_dictionary()
for word in dictionary:
    print(word + ": ")
    print(dictionary[word])
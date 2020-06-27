#########################################################################################
#
#                                 Naive Bayes Classifier
#   Joshua Pickard                                                          June 2020
#   jpic@umich.edu
#
#   Purpose: 
#
#   Class attributes:
#       1. dictionary
#       2. regular
#       3. disaster
#   
#   Methods:
#       - constructor
#       - classify
#       - probability
#       - log_prior
#       - log_liklihood
#       - word_not_in_class
#       - word_not_defined
#
#########################################################################################

class Cnaive_bayes:

    def __init__(self, data_cleaner):
        self.dictionary = data_cleaner.dictionary
        self.regular = data_cleaner.regular
        self.disaster = data_cleaner.disaster
        














#########################################################################################
#
#                                 Naive Bayes Classifier
#   Joshua Pickard                                                          June 2020
#   jpic@umich.edu
#
#   Purpose: 
#
#   Class attributes:
#       1. dictionary...stores all of the words used in the training dataset and the 
#                       number of occurences of each word in each set
#       2. catagories...stores the list of all catagories and the number of occurences
#                       of a message from each category
#       3. messsages....stores a list of all the training data messages
#   
#   Methods:
#       - __init__
#       - build_dictionary
#       - format
#       - newWord
#       - print_dictionary
#
#       - predict
#       - probability
#       - log_prior
#       - log_likelihood
#       - word_not_in_class
#       - word_not_defined
#
#########################################################################################
import re
import math
from data_cleaner import Cdata_cleaner
from tweet import Ctweet

class Cnaive_bayes:

    def __init__(self, data_cleaner):
        self.messages = data_cleaner.getMessages()
        self.catagories = data_cleaner.getCatagories()
        self.total_posts = 0
        for x in self.catagories:
            self.total_posts = self.total_posts + self.catagories[x]
        self.build_dictionary()

    def build_dictionary(self):
        self.dictionary = dict()
        for message in self.messages:
            if message.validate():
                list_of_words = message.getText().split()
                formated_words = list()
                for word in list_of_words:
                    formated_words.append(self.format(word))
                remove_duplicates = set(formated_words)
                for formated_word in remove_duplicates:
                    if formated_word not in self.dictionary:
                        self.dictionary[formated_word] = self.category_values()
                    self.dictionary[formated_word][message.getTarget()] = self.dictionary[formated_word][message.getTarget()] + 1
    
    def format(self, word):
        if len(word) > 4 and word[0:4] == "http":
            return "1234http5678link"
        else:
            word = word.lower()
            return re.sub('[\W_]', '', word)

    def category_values(self):
        ret = dict()
        for category in self.catagories:
            ret[category] = 0
        return ret

    def print_dictionary(self):
        keys = list()
        for word in self.dictionary:
            keys.append(word)
        keys.sort()
        for word in keys:
            print(word, self.dictionary[word])

    def predict_label(self, message):
        category_probabilities = self.category_values()
        for label in category_probabilities:
            category_probabilities[label] = self.probability(message, label)
        sorted_categories = list()
        for word in category_probabilities:
            sorted_categories.append(word)
        sorted_categories.sort()
        max_probability = category_probabilities[sorted_categories[0]]
        best_label = sorted_categories[0]
        for category in sorted_categories:
            if category_probabilities[category] > max_probability:
                max_probability = category_probabilities[category]
                best_label = category
        return (best_label, max_probability)

    def probability(self, message, label):
        probability = self.prob_log_prior(label)
        sorted_list = list()
        for word in message.getText().split():
            sorted_list.append(word)
        sorted_list.sort()
        previous_word = ""
        for word in sorted_list:
            if word != previous_word:
                formated_word = self.format(word)
                add = 0.0
                if formated_word in self.dictionary and int(self.dictionary[formated_word][label]) != 0:
                    add = self.prob_log_likelihood(formated_word, label)
                elif formated_word in self.dictionary:
                    add = self.prob_not_seen_with_label(formated_word, label)
                else:
                    add =  self.prob_not_seen()
                #print(" " + word + ":" + str(round(add,2)), end = "")
                probability = probability + add
                previous_word = word
        #print("=" + str(round(probability,2)))
        return probability
    
    def prob_log_prior(self, label):
        return math.log(self.catagories[label]/self.total_posts)

    def prob_log_likelihood(self, word, label):
        return math.log(self.dictionary[word][label]/self.catagories[label])

    def prob_not_seen_with_label(self, word, label):
        occurences = 0
        for label in self.dictionary[word]:
            occurences = occurences + self.dictionary[word][label]
        return math.log(occurences/self.total_posts)

    def prob_not_seen(self):
        return math.log(1/self.total_posts)

    def classify(self, message_list):
        print("test data:")
        correct = 0
        for message in message_list:
            assignment = self.predict_label(message)
            label = assignment[0]
            probability = assignment[1]
            print("  correct = " + message.getTarget() + ", predicted = " + label + ", log-probability score = " + str(probability))
            print("  content = " + message.getText())
            print("")
            if message.getTarget() == label:
                correct = correct + 1
        print("performance: " + str(correct) + "/" + str(len(message_list)) + " posts predicted correctly")
        return correct
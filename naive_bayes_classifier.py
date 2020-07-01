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
#                       number of occurences of each word in each category of post. A
#                       word occuring multiple times in 1 post is only counted once.
#       2. catagories...stores the list of all catagories and the number of occurences
#                       of a message from each category
#       3. messsages....stores a list of all the training data messages
#   
#   Methods:
#       - __init__...................initializes messages and catagories and immediatly
#                                    calls build_dictionary
#       - build_dictionary...........constructs dictionary according to the rules above
#       - format.....................makes all words lowercase, removes nonalphnumeric
#                                    characters, and converts all links to the same 
#                                    string ("1234http5678link")
#       - category_values............returns a dictionary where each category in
#                                    catagories is a key and has a value of 0
#       - print_dictionary...........prints the dictionary alphabetically
#       - predict_label..............predicts the catagory of a Ctweet
#       - probability................determins the probability that a Ctweet is a specfic
#                                    category
#       - prob_log_prior.............probability that any message is in a specific
#                                    category
#       - prob_log_likelihood........conditional probability that a message with a word
#                                    is in a given category. This is used when messages 
#                                    has at least 1 Ctweet with the given label and word
#                                    in question
#       - prob_not_seen_with_label...probability that a message with a word is in a given
#                                    category. This is used when prob_log_likelihood 
#                                    can't be used, but message does contain a Ctweet 
#                                    with the given word.
#       - prob_not_seen..............probability that a message with a word is in a given
#                                    category. This is used when the word never appeard
#                                    in a Ctweet in messages.
#       - classify...................This is used classify a whole list of tweets
#
#   References:
#       - https://eecs280staff.github.io/p5-ml/naive_bayes.html
#       - https://nlp.stanford.edu/IR-book/html/htmledition/naive-bayes-text-
#         classification-1.html
#
#########################################################################################
import re
import math
from data_cleaner import Cdata_cleaner
from tweet import Ctweet

class Cnaive_bayes:

    #####################################################################################
    #
    #   Cnaive_bayes:__init__
    #       Parameters: 1. data_cleaner: the data cleaner used to read in thraining data
    #                                    for this classifier
    #
    #       Description: Initializes messages and catagories based on the data_cleaner. 
    #                    After that, dictionary is impediatly build with a call to 
    #                    build_dictionary
    #
    #####################################################################################
    def __init__(self, data_cleaner):
        self.messages = data_cleaner.getMessages()
        self.catagories = data_cleaner.getCatagories()
        self.build_dictionary()

    #####################################################################################
    #
    #   Cnaive_bayes:build_dictionary
    #       Description: Creates and fills dictionary based on messages. For every word
    #                    found in a message in messages, dictionary stores the word as a
    #                    key (key 1) with a value that is another dictionary which 
    #                    contains each catagory as another key (key 2) with a value of 
    #                    the number of times that word (key 1) occured in a message of 
    #                    the catagory (key 2).
    #       
    #       Note: 1) A word that occurs multiplee times in a post is only tallied once in
    #                the dictionary for that post. 
    #             2) All words are preformated according the the format method prior to 
    #                being entered into dictionary.
    #
    #####################################################################################
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
                    self.dictionary[formated_word][message.getTarget()] = \
                        self.dictionary[formated_word][message.getTarget()] + 1
    
    #####################################################################################
    #
    #   Cnaive_bayes:format
    #       Parameters: 1. word: the word to be reformated
    #
    #       Returns: formated word
    #
    #       Description: This method returns a formated word, which is a lowercase word
    #                    with all nonalphanumeric characters removes or if it is a link
    #                    the formated word is "1234http5678link". All links are converted
    #                    to the same string because it is very unlikely that 2 messages
    #                    contain the exact same link, but messages that contain links 
    #                    still have similar characteristics, so uniforming how the link
    #                    is recorded takes this into account.
    #     
    #####################################################################################
    def format(self, word):
        if len(word) > 4 and word[0:4] == "http":
            return "1234http5678link"
        else:
            word = word.lower()
            return re.sub('[\W_]', '', word)
    
    #####################################################################################
    #
    #   Cnaive_bayes:category_values
    #       Returns: a dictionary where each category is a key with a value of 0
    #     
    #####################################################################################
    def category_values(self):
        ret = dict()
        for category in self.catagories:
            ret[category] = 0
        return ret

    #####################################################################################
    #
    #   Cnaive_bayes:print_dictionary
    #       Description: Prints the dictionary with the keys listed alphabetically as
    #                    follows: 
    #                   
    #                       word {'catagory 1': occurences, 'catagory 2': occurences,...}
    #                               
    #       References: 1. in naive_bayes_test.py see simple_dictionary
    #                   2. the dictionary defined by family_dictionary_test.csv is
    #                      correctly printed to faily_dictionary_test_correct.txt
    #     
    #####################################################################################
    def print_dictionary(self):
        keys = list()
        for word in self.dictionary:
            keys.append(word)
        keys.sort()
        for word in keys:
            print(word, self.dictionary[word])

    #####################################################################################
    #
    #   Cnaive_bayes:predict_label
    #       Parameters: 1. message: the message to be labeled
    #
    #       Returns: A tuple containing [0] the predicted label and [1] the probability
    #                that that label is correct
    #
    #       Description: For each catagory in catagories, the probability of that
    #                    caragory being the correct label is computed. Then, the catagory
    #                    with the maximum probability along with the probability is 
    #                    returned as a tuple.
    #                               
    #####################################################################################
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

    #####################################################################################
    #
    #   Cnaive_bayes:probability
    #       Parameters: 1. message: the message thats probability is being computed for 
    #                               the given label
    #                   2. label: the label being used to compute the probability
    #
    #       Returns: The probability that the label is correct
    #
    #       Description: The probability that the message has the label is computed using
    #                    the sum of 2 things:
    #                       1. log_prior: the probability based purly on the label
    #                       2. For each word in message.getText, the words connditional
    #                          probability that the word is associated with the label is
    #                          computed using:
    #                            a) prob_log_likelihood
    #                            b) prob_not_seen_with_label
    #                            c) prob_not_seen
    #                          depending on the word's presence in the training data and
    #                          dictionary.
    #                               
    #####################################################################################
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
                if formated_word in self.dictionary and \
                    int(self.dictionary[formated_word][label]) != 0:
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

    #####################################################################################
    #
    #   Cnaive_bayes:prob_log_prior
    #       Parameters: 1. label: the label being used to compute the probability
    #
    #       Returns: ln(number of posts with the label / total number of training posts)
    #
    #       Description: Used in computing the probability of all posts
    #                               
    #####################################################################################
    def prob_log_prior(self, label):
        return math.log(self.catagories[label]/len(self.messages))


    #####################################################################################
    #
    #   Cnaive_bayes:prob_log_likelihood
    #       Parameters: 1. word: The word that the conditional probability is being
    #                            computed for based on the label
    #                   2. label: The label being used to compute the probability
    #
    #       Returns: ln(number of posts with word and label / number of posts with label)
    #
    #       Description: Used in computing the probability of a message having a given
    #                    label when a given word is in the message and the word was seen
    #                    in a message with the label in the dictionary
    #                               
    #####################################################################################
    def prob_log_likelihood(self, word, label):
        return math.log(self.dictionary[word][label]/self.catagories[label])

    #####################################################################################
    #
    #   Cnaive_bayes:prob_not_seen_with_label
    #       Parameters: 1. word: The word that the conditional probability is being
    #                            computed for based on the label
    #                   2. label: The label being used to compute the probability
    #
    #       Returns: ln(number of posts with word / total number of training posts)
    #
    #       Description: This is used in computing the probability of a message having a
    #                    given label when a given word is in the message and the word was
    #                    seen in a message but not in a message with the label.
    #                               
    #####################################################################################
    def prob_not_seen_with_label(self, word, label):
        occurences = 0
        for label in self.dictionary[word]:
            occurences = occurences + self.dictionary[word][label]
        return math.log(occurences/len(self.messages))

    #####################################################################################
    #
    #   Cnaive_bayes:prob_not_seen
    #       Returns: ln(1 / total number of training posts)
    #
    #       Description: When a word is seen in the test set but not the training set, 
    #                    this method is used in computing the probability of the message
    #                    the word appears in.
    #                               
    #####################################################################################
    def prob_not_seen(self):
        return math.log(1/len(self.messages))

    #####################################################################################
    #
    #   Cnaive_bayes:classify
    #       Parameters: 1. message_list: a list of messages to have their label's
    #                                    predicted
    #
    #       Returns: A tuple containing [0] the number of correctly classified posts and
    #               [1] the number of classified posts
    #
    #       Description: It predicts the label of each message in message_list.
    #                               
    #####################################################################################
    def classify(self, message_list):
        print("test data:")
        correct = 0
        for message in message_list:
            assignment = self.predict_label(message)
            label = assignment[0]
            probability = assignment[1]
            print("  correct = " + message.getTarget() + ", predicted = " + label + ", \
                log-probability score = " + str(probability))
            print("  content = " + message.getText())
            print("")
            if message.getTarget() == label:
                correct = correct + 1
        print("performance: " + str(correct) + "/" + str(len(message_list)) + \
            " posts predicted correctly")
        return (correct, len(message_list))

# END Cnaive_bayes class definition
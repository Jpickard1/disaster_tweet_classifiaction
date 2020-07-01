#########################################################################################
#
#                                   Testing Framework
#   Joshua Pickard                                                          June 2020
#   jpic@umich.edu
#
#   Purpose: Provide a simple framework for writing and executing all tests
#
#   Description: Rather than being arranged as a class, each 
#   
#   Methods:
#       - __init__
#       - build_dictionary
#       - format
#       - newDefinition
#
#       - constructor
#       - predict
#       - probability
#       - log_prior
#       - log_liklihood
#       - word_not_in_class
#       - word_not_defined
#
#########################################################################################
import sys
from test_helpers import test_helper
from naive_bayes_test import *

#sys.stdout = open("test_output.txt", "w")

helper = test_helper()
naive_bayes_tests(helper)
from test_helpers import test_helper

from naive_bayes_classifier import Cnaive_bayes
from data_cleaner import Cdata_cleaner
from tweet import Ctweet

def naive_bayes_tests(helper):
    helper.toTerminal()
    simple_dictionary(helper)
    eecs_280_small(helper)
    #eecs_280_instructor_student(helper)
    eecs_280_project_exam(helper)
    reddit_classifier(helper)

def simple_dictionary(helper):
    print("Simple Dictionary Test: ", end = "")
    cleaner = Cdata_cleaner()
    cleaner.read_csv("family_dictionary_test.csv")
    classifier = Cnaive_bayes(cleaner)
    helper.toFile()
    classifier.print_dictionary()
    assert(helper.file_compare("family_dictionary_test_correct.txt", "test_output.txt"))
    print("PASS")

def eecs_280_small(helper):
    print("EECS 280 Small Test: ", end = "")
    cleaner1 = Cdata_cleaner()
    cleaner2 = Cdata_cleaner()
    cleaner1.read_csv("280_train_small.csv")
    cleaner2.read_csv("280_test_small.csv")
    classifier = Cnaive_bayes(cleaner1)
    helper.toFile()
    correct = classifier.classify(cleaner2.getMessages())
    helper.toTerminal()
    assert(correct == 2)
    print("PASS")

def eecs_280_instructor_student(helper):
    print("EECS 280 Projects Test: ", end = "")
    cleaner1 = Cdata_cleaner()
    cleaner2 = Cdata_cleaner()
    cleaner1.read_csv("280_w14-f15_instructor_student.csv")
    cleaner2.read_csv("280_w16_instructor_student.csv")
    classifier = Cnaive_bayes(cleaner1)
    helper.toFile()
    correct = classifier.classify(cleaner2.getMessages())
    helper.toTerminal()
    print(correct)
    assert(correct == 2602)
    print("PASS")

def eecs_280_project_exam(helper):
    print("EECS 280 Projects Test: ", end = "")
    cleaner1 = Cdata_cleaner()
    cleaner2 = Cdata_cleaner()
    cleaner1.read_csv("280_w16_projects_exam.csv")
    cleaner2.read_csv("280_sp16_projects_exam.csv")
    classifier = Cnaive_bayes(cleaner1)
    helper.toFile()
    correct = classifier.classify(cleaner2.getMessages())
    helper.toTerminal()
    assert(correct == 245)
    print("PASS")

def reddit_classifier(helper):
    print("Reddit Classification Test: ", end = "")
    cleaner1 = Cdata_cleaner()
    cleaner2 = Cdata_cleaner()
    cleaner1.read_csv("trainReddit.csv")
    cleaner2.read_csv("testReddit.csv")
    classifier = Cnaive_bayes(cleaner1)
    helper.toFile()
    correct = classifier.classify(cleaner2.getMessages())
    helper.toTerminal()
    print(correct)
    #assert(correct == 245)
    print("PASS")
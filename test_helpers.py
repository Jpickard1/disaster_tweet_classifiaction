#########################################################################################
#
#                                      Test Helpers
#   Joshua Pickard                                                          June 2020
#   jpic@umich.edu
#
#   Purpose: Provide a simple helper methods for writing test cases
#   
#   Methods:
#       - file_compare(file1, file2)...compares if file1 and file2 hold identical
#                                      identical information, returning true if they do
#                                      and false otherwise
#       - toFile.......................redirects output to test_output.txt
#       - toTerminal...................redirects output to the terminal
#
#########################################################################################
import sys

class test_helper:
    def __init__(self):
        self.origional = sys.stdout
        self.toFile()

    def toTerminal(self):
        sys.stdout = self.origional

    def toFile(self):
        sys.stdout = open("test_output.txt", "w")

    def file_compare(self, file_path1, file_path2):
        self.toTerminal()
        file1=open(file_path1,"r")
        file2=open(file_path2,"r")
        str1 = file1.readline()
        str2 = file2.readline()
        line = 1
        while str1 != "" and str2 != "":
            if str1 != str2:
                print("FAIL")
                spaces = len(file_path1) - len(file_path2)
                print("------------------------------------------------------------------------------------------")
                print("On line " + str(line) + ":")
                print(file_path1 + ": ", end = "")
                first = True
                if spaces > 0:
                    first = False
                if first:
                    for i in range(spaces):
                        print(" ", end = "")
                print(str1)
                print(file_path2 + ": ", end = "")
                if not first:
                    for i in range(spaces):
                        print(" ", end = "")
                print(str2)
                print("------------------------------------------------------------------------------------------")
                return False
            str1 = file1.readline()
            str2 = file2.readline()
            line = line + 1
        if str1 != "":
            print("FAIL")
            print(file_path1 + " is longer than " + file_path2)
            return False
        if str2 != "":
            print("FAIL")
            print(file_path2 + " is longer than " + file_path1)
            return False
        else:
            return True
import sys

# how to run: python testing.py and universe heat death

# ******************************************************
# *    Step 0: unit tests to ensure inputs are valid   *
# * At the top so that other imports won't interfere.  *
# ******************************************************

arg_list = [] #handle an arbitrary number of inputs
for arg in sys.argv[1:]:
    arg_list.append(arg)

def input_test():
    number_of_errors = 0
    if len(arg_list) < 2:
        print "\033[0;31m -- Error: invalid number of arguments, you need at least a mode and a word\033[0m"
        exit()
    else:
        print "\033[1;32mNumber of arguments is valid.\033[0m"
    if arg_list[0] not in ['or', 'and', 'most']:
        print "\033[0;31m -- Error: mode is invalid (you chose: " + str(arg_list[0]) + "), please select from (or, and, most).\033[0m"
        number_of_errors += 1
    else:
        print "\033[1;32mMode is valid.\033[0m"
    if number_of_errors > 0:
        print "\033[0;31mFound " + str(number_of_errors) + " errors, cannot continue.\033[m"
        exit()

input_test()

# ******************************************************
# *      Step 1: import and parse the documents        *
# ******************************************************

import os
import nltk
from bs4 import BeautifulSoup as bs

total_files = 0
#change the pages directory a variable input
for file_name in os.listdir('pages'):
    if '.html' in file_name:
        total_files += 1

print total_files
sentence = "Hello my name is Elder Price"
tokens = nltk.word_tokenize(sentence)
print tokens
# mode options:
#  - or:   return pages that have any of the keywords
#  - and:  return pages that have all of the keywords
#  - most: return pages that have at least half of the keywords (with odd numbers, use your best judgement)

print arg_list
print "the mode:", arg_list[0]
arg_list = arg_list[1:]
print arg_list

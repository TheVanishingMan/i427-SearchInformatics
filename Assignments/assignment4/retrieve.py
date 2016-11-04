import sys, os

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
    if os.path.isfile('docs.dat') and os.path.isfile('invindex.dat'):
        print "\033[1;32mFound docs.dat and invindex.dat\033[0m"
    else:
        print "\033[0;31m -- Error: missing files, you need docs.dat and invindex.dat. Did you forget to ./buildindex.sh?\033[0m"
        number_of_errors += 1
    if number_of_errors > 0:
        print "\033[0;31mFound " + str(number_of_errors) + " errors, cannot continue.\033[m"
        exit()

input_test()

# ******************************************************
# *      Step 1: import and parse the documents        *
# *             docs.dat and invindex.dat              *
# ******************************************************

import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *

print arg_list
mode = arg_list[0]
print "the mode:", mode
arg_list = arg_list[1:]
print arg_list

stemmer = PorterStemmer()
filtered_words = [word for word in arg_list if word not in stopwords.words('english')]
stemmed_words = [stemmer.stem(word) for word in filtered_words]
list_of_word_strings = [str(word) for word in stemmed_words]
#list_of_word_strings now contains all the words we need to query in the inverted index
print "stemmed and filtered: " + str(list_of_word_strings)

inverted_index_dict = {}
with open('invindex.dat') as inverted_index:
    inverted_index_list = inverted_index.readlines()

for line in inverted_index_list:
    content = line.split()
    word = str(content[0])
    documents_as_string = ""
    for item in content[2:]:
        documents_as_string = documents_as_string + str(item) + ' '
    inverted_index_dict[word] = documents_as_string

print len(inverted_index_dict)

document_data_dict = {}
with open('docs.dat') as doc_data:
    document_data_list = doc_data.readlines()

for line in document_data_list:
    content = line.split()
    key = str(content[0])
    document_info = ""
    for item in content[1:]:
        document_info = document_info + str(item) + ' '
    document_data_dict[key] = document_info

#inverted_index_dict = {}
#document_data_dict = {}

if mode == 'or':
    fixed_list = set()
    for word in list_of_word_strings:
        text_list = inverted_index_dict.get(word).split()
        for item in text_list:
            head, sep, tail = item.partition(':')
            fixed_list.add(head)
    print fixed_list
    print len(fixed_list)
elif mode == 'and':
    fixed_list = set()
    #find the first word from user input
    first_word = list_of_word_strings[0]
    #pop it off the front
    list_of_word_strings = list_of_word_strings[1:]
    text_list = inverted_index_dict.get(first_word).split()
    for item in text_list:
        head, sep, tail = item.partition(':')
        fixed_list.add(head)
    new_set = set()
    for word in list_of_word_strings:
        text_list = inverted_index_dict.get(word).split()
        for item in text_list:
            head, sep, tail = item.partition(':')
            new_set.add(head)
        fixed_list = new_set.intersection(fixed_list)
                
    print fixed_list
    print len(fixed_list)
        

#print len(document_data_dict)
#print document_data_dict['5.html']
#print document_data_dict.keys()

#modes:
#  - or:   return pages that have any of the keywords
#  - and:  return pages that have all of the keywords
#  - most: return pages that have at least half of the keywords (with odd numbers, use your best judgement)



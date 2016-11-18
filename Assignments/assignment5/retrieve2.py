import sys, os, math

# how to run: python retrieve2.py word1 word2 word3 ...

# ******************************************************
# *    Step 0: unit tests to ensure inputs are valid   *
# * At the top so that other imports won't interfere.  *
# ******************************************************

arg_list = [] #handle an arbitrary number of inputs
for arg in sys.argv[1:]:
    arg_list.append(arg)

def input_test():
    number_of_errors = 0
    if len(arg_list) < 1:
        print "\033[0;31m -- Error: invalid number of arguments, you need at least one word\033[0m"
        exit()
    else:
        print "\033[1;32mNumber of arguments is valid.\033[0m"
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

stemmer = PorterStemmer()
filtered_words = [word for word in arg_list if word not in stopwords.words('english')]
stemmed_words = [stemmer.stem(word) for word in filtered_words]
list_of_word_strings = [str(word) for word in stemmed_words]
#list_of_word_strings now contains all the words we need to query in the inverted index
#print "stemmed and filtered: " + str(list_of_word_strings)

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

#print len(inverted_index_dict)

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

documents_explored = 0

most_dict = {}
for html_doc in document_data_dict.keys():
    for word in list_of_word_strings:
        if inverted_index_dict.has_key(word):
            text_list = inverted_index_dict[word].split()
            for item in text_list:
                documents_explored += 1
                head, sep, tail = item.partition(':')
                if head == html_doc:
                    if most_dict.has_key(head):
                        most_dict[head] += 1
                    else:
                        most_dict[head] = 1
# "selecting elements of python dictionary greater than a certain value"
stripped_most_dict = dict((k, v) for k, v in most_dict.items() if v >= int(math.ceil(len(list_of_word_strings)/2)))
fixed_list = []
for key in stripped_most_dict:
    #print key
    fixed_list.append(key)

#print most_dict
#    print fixed_list
#    print len(fixed_list)
int_to_print = 1
print "\033[1;32m\n\nSuper-Google Results:\033[0m"
for item in fixed_list:
    final_list = document_data_dict[item].split()
    url_to_print = final_list[2]
    title_to_print = final_list[1]
    print '  ' + str(int_to_print) + ') ' + url_to_print + '  -----  ' + title_to_print.replace('_',' ')
    int_to_print += 1
print "Explored " + str(documents_explored) + " documents and found " + str(int_to_print-1) + " results."

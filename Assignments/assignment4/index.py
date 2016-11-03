import sys, os

# ******************************************************
# *    Step 0: unit tests to ensure inputs are valid   *
# * At the top so that other imports won't interfere.  *
# ******************************************************

# http://stackabuse.com/python-check-if-a-file-or-directory-exists/

arg_list = []
for arg in sys.argv[1:]:
    arg_list.append(arg)

def input_test():
    global directory, index, path_to_file
    number_of_errors = 0
    if len(arg_list) < 2:
        print "\033[0;31m -- Error: invalid number of arguments, please specify a directory/ and an index.dat file\033[0m"
        exit()
    else:
        print "\033[1;32mNumber of arguments is valid.\033[0m"
    if not arg_list[0].endswith('/'):
        print "\033[0;31m -- Error: not a valid directory (you chose: " + str(arg_list[0]) + "), did you forget to include a '/' at the end?\033[0m"
        number_of_errors += 1
    else:
        print "\033[1;32mDirectory is valid.\033[0m"
        directory = str(arg_list[0])
        index = str(arg_list[1])
        path_to_file = directory + index
        if os.path.isfile(path_to_file):
            print "\033[1;32mFile and the path to it are valid.\033[m"
        else:
            print "\033[0;31m -- Error: either the path is incorrect, the file is incorrect, or both.\033[m"
            print "\033[0;31m --        Tried to access a file at: " + path_to_file + "\033[m"
            number_of_errors += 1
    if number_of_errors > 0:
        print "\033[0;31mFound " + str(number_of_errors) + " errors, cannot continue.\033[m"
        exit()

input_test()
print "\n\033[1;32mAll tests passed successfully!\033[0m"

print directory
print index
print path_to_file

with open(path_to_file) as file_to_read:
    html_file = file_to_read.readlines()

for line in html_file:
    print line.split()

import re, string, nltk
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.stem.porter import *

# http://stackoverflow.com/questions/1936466/beautifulsoup-grab-visible-webpage-text
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# http://stackoverflow.com/questions/8689795/how-can-i-remove-non-ascii-characters-but-leave-periods-and-spaces-using-python
# http://stackoverflow.com/questions/5486337/how-to-remove-stop-words-using-nltk-or-python
# http://www.nltk.org/howto/stem.html
'''
html_file = sys.argv[1]
html_file = open(html_file).read()
doc = html_file.replace('&nbsp;', ' ')
doc = doc.replace('\n', ' ')
#soup = BeautifulSoup(doc, 'html.parser')
soup = BeautifulSoup(doc, 'lxml')
data = soup.findAll(text=True)
title = ""

def visible(element):
    if element.parent.name in ['title']:
        global title
        title = str(element)
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element.encode('utf-8'))):
        return False
    return True

visible_text = filter(visible, data)
printable = set(string.printable)
new_word = ""

for item in visible_text:
    for letter in item:
        if letter in printable:
            new_word = new_word + letter.lower()

word_list = nltk.word_tokenize(new_word)
filtered_words = [word for word in word_list if word not in stopwords.words('english')]
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_words]

print "Title:  " + title
print "Length: " + str(len(stemmed_words))
for item in stemmed_words:
    print item,
'''

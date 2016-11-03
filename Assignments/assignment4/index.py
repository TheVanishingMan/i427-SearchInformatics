import sys, os, re, string, nltk
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.stem.porter import *

directory = sys.argv[1]
index = sys.argv[2]

print directory
print index

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

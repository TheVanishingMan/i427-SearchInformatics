# IMPORTANT:
# run the file with: `python2.7 a2.py test.txt`
import nltk
import os
import sys

# this can be changed into a loop through the directory
# refer to https://github.iu.edu/hayesall/STARAI-financial-nlp/extractFinancialLines.py
# code I've written there has some really useful features that can be implemented here.
input_file = sys.argv[1]
f = open(input_file, 'r')
document_string = f.read().splitlines()
split_document_string = document_string[0].split(" ")
print document_string
print split_document_string
print "Document " + str(input_file) + " is " + str(len(split_document_string)) + " words long."
f.close()

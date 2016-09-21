# IMPORTANT:
# run the file with: `python2.7 a2.py test.txt`
import nltk, os, sys

#originally I defined these as separate methods:
'''
def numberOfSentences(ls):
    sentences = 0
    for word in ls:
        if '.' in word:
            sentences += 1
    return sentences

def numberOfLetters(ls):
    words = 0
    for word in ls:
        words += len(word)
    return words
'''

#but it seems inefficient to go through an array twice.
#I rewrote the function to be single pass, it only has
#to return an array where the first element is numLetters
#and the second element is numSentences.

#I might still change this so I can go: 'parseForLettersAndSentences.letters()'
def parseForLettersAndSentences(ls):
    letters = 0
    sentences = 0
    for word in ls: #previously this loop was executed twice (across two functions)
        letters += len(word) #short term we go from O(2n) --> O(n)
        if '.' in word: #speedup will only be apparent as number of documents grows.
            sentences += 1
    return [letters, sentences]

# this can be changed into a loop through the directory
# refer to https://github.iu.edu/hayesall/STARAI-financial-nlp/extractFinancialLines.py
# code I've written there has some really useful features that can be implemented here.
input_file = sys.argv[1]
f = open(input_file, 'r')
document_string = f.read().splitlines()
split_document_string = document_string[0].split(" ")
number_of_words = len(split_document_string)
testoutput = parseForLettersAndSentences(split_document_string)
number_of_sentences = testoutput[1]
number_of_letters = testoutput[0]
coleman_liau = (5.88*number_of_letters/number_of_words)-(29.6*number_of_sentences/number_of_words)-15.8

#print document_string
#print split_document_string
print "Analyzing " + str(input_file) + ":"
#print "Document " + str(input_file) + " has " + str(number_of_sentences) + " sentences."
print "  Number of words: " + str(number_of_words)
print "  Number of sentences: " + str(number_of_sentences)
print "  CL level: " + str(coleman_liau)

#print testoutput
#print "Document " + str(input_file) + " is " + str(number_of_words) + " words long."
#print "Coleman-Liau index of " + str(input_file) + " is " + str(coleman_liau) + "."
f.close()

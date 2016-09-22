# IMPORTANT:
# run the file with: `python2.7 a2.py test.txt`
import nltk, os, sys

#I might still change this so I can go: 'parseForLettersAndSentences.letters()'
def parseForLettersAndSentences(ls):
    letters = 0
    sentences = 0
    for word in ls: #previously this loop was executed twice (across two functions)
        letters += len(word) #short term we go from O(2n) --> O(n)
        if '.' in word: #it's a very small improvement, but it is an improvement
            sentences += 1
    return [letters, sentences]

def parseForVowelsAndDipthongs(ls):
    vowels = 0
    dipthongs = 0
    for word in ls:
        for letter in word.lower():
            condA = letter=='a'
            condE = letter=='e'
            condI = letter=='i'
            condO = letter=='o'
            condU = letter=='u'
            if condA or condE or condI or condO or condU:
                vowels += 1
    return vowels

# this can be changed into a loop through the directory
# refer to https://github.iu.edu/hayesall/STARAI-financial-nlp/extractFinancialLines.py
# code I've written there has some really useful features that can be implemented here.
input_file = sys.argv[1]
f = open(input_file, 'r')
document_string = f.read().splitlines()
split_document_string = document_string[0].split(" ")
number_of_words = len(split_document_string)


letters_and_sentences = parseForLettersAndSentences(split_document_string)
number_of_sentences = letters_and_sentences[1]
number_of_letters = letters_and_sentences[0]


if number_of_words==0: #in case of emergency, prevent divide by zero errors
    number_of_words = 1
coleman_liau = (5.88*number_of_letters/number_of_words)-(29.6*number_of_sentences/number_of_words)-15.8


number_of_vowels = parseForVowelsAndDipthongs(split_document_string)



#Return values
#print document_string
#print split_document_string
print "Analyzing the document" #+ str(input_file) + ":"
#print "Document " + str(input_file) + " has " + str(number_of_sentences) + " sentences."
print "  Number of words:     " + str(number_of_words)
print "  Number of sentences: " + str(number_of_sentences)
print "  CL level:            " + str(coleman_liau)
print "  Vowels:              " + str(number_of_vowels)

#print testoutput
#print "Document " + str(input_file) + " is " + str(number_of_words) + " words long."
#print "Coleman-Liau index of " + str(input_file) + " is " + str(coleman_liau) + "."
f.close()

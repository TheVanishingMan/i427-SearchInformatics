# IMPORTANT:
# run the file with: `python2.7 a2.py test.txt`
import nltk, os, sys

def parseForLSVD(ls): #letters, sentences, vowels, and dipthongs
    letters, sentences, vowels, dipthongs = 0,0,0,0
    vowel_set = 'aeiou'
    for word in ls:
        previous_letter = '@'
        letters += len(word)
        if '.' in word:
            sentences += 1
        for letter in word.lower():
            condA = letter=='a'
            condE = letter=='e'
            condI = letter=='i'
            condO = letter=='o'
            condU = letter=='u'
            if condA or condE or condI or condO or condU:
                vowels += 1
                if previous_letter in vowel_set:
                    dipthongs += 1
            previous_letter = letter
    return [letters, sentences, vowels, dipthongs]

# this can be changed into a loop through the directory
# refer to https://github.iu.edu/hayesall/STARAI-financial-nlp/extractFinancialLines.py
# code I've written there has some really useful features that can be implemented here.
input_file = sys.argv[1]
f = open(input_file, 'r')
document_string = f.read().splitlines()
split_document_string = document_string[0].split(" ")
number_of_words = len(split_document_string)

LSVD=parseForLSVD(split_document_string)
number_of_letters = LSVD[0]
number_of_sentences = LSVD[1]

if number_of_words==0: #in case of emergency, prevent divide by zero errors
    number_of_words = 1
coleman_liau = (5.88*number_of_letters/number_of_words)-(29.6*number_of_sentences/number_of_words)-15.8

number_of_vowels = LSVD[2]
number_of_dipthongs = LSVD[3]
number_of_syllables = number_of_vowels - number_of_dipthongs

flesch_kincaid = (0.39*number_of_words/number_of_sentences)+(11.8*number_of_syllables/number_of_words)-15.59


#Return values
#print document_string
#print split_document_string
print "Analyzing the document" #+ str(input_file) + ":"
#print "Document " + str(input_file) + " has " + str(number_of_sentences) + " sentences."
print "  Number of words:     " + str(number_of_words)
print "  Number of sentences: " + str(number_of_sentences)
print "  CL level:            " + str(coleman_liau)
#print "  Vowels:              " + str(number_of_vowels)
#print "  Dipthongs:           " + str(number_of_dipthongs)
print "  Syllables~:          " + str(number_of_syllables)
print "  FK Score:            " + str(flesch_kincaid)

#print testoutput
#print "Document " + str(input_file) + " is " + str(number_of_words) + " words long."
#print "Coleman-Liau index of " + str(input_file) + " is " + str(coleman_liau) + "."
f.close()

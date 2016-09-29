# This can be changed to loop through the contents of a directory, a shell script will be quicker
# for me to write (and debug if necessary) though.
# refer to https://github.iu.edu/hayesall/STARAI-financial-nlp/src/extractFinancialLines.py

# IMPORTANT:
# run the file with: `python2.7 a2.py test.txt`
# or `./script.sh part1_test_documents`
# or `bash script.sh part1_test_documents`

import nltk, os, sys

# letters can be improved with the predicate 'isLetter()'
def parseForLSVD(ls): #letters, sentences, vowels, and dipthongs
    letters, sentences, vowels, dipthongs = 0,0,0,0
    vowel_set = 'aeiou'
    for word in ls:
        previous_letter = '@' # It doesn't really matter what this character is at the beginning of the loop.
        letters += len(word)  # The only thing that really matters is that it is not a vowel, and that it gets reset
        if '.' in word:       # each time we begin a new word.
            sentences += 1
        for letter in word.lower(): # still needs a check for if the word ends in 'e'
            condA = letter=='a' # http://stackoverflow.com/questions/19954593/python-checking-a-strings-first-and-last-character
            condE = letter=='e' # create a separate variable for handling vowels in an individual word (dependent on where the vowels are).
            condI = letter=='i'
            condO = letter=='o'
            condU = letter=='u'
            if condA or condE or condI or condO or condU:
                vowels += 1
                if previous_letter in vowel_set:
                    dipthongs += 1
            previous_letter = letter
    return [letters, sentences, vowels, dipthongs]


# I use an input file where all of the text is on one line.
# There's probably a cleaner way but for other applications
# I've written this makes things easier in the long run.
# To pull this off, I preprocess the text files with a bash
# script (using a trick with the built-in echo command).

# Part 1: Handling the input
input_file = sys.argv[1]
f = open(input_file, 'r')
document_string = f.read().splitlines()
split_document_string = document_string[0].split(" ")

# Question 1: "Number of Words" in document
number_of_words = len(split_document_string)

# Question 2: "Number of Sentences" in document
# maybe calculate number of sentences by checking if a word ends in a !.? and the next word starts with a capital?
LSVD=parseForLSVD(split_document_string)
number_of_letters = LSVD[0]
number_of_sentences = LSVD[1]

# Question 3: "Calculate the Coleman-Liau index" (approximate grade level)
if number_of_words==0: #in case of emergency, prevent divide by zero errors
    number_of_words = 1
    print "POSSIBLE ERROR--attempted to divide by zero."
coleman_liau = (5.88*number_of_letters/number_of_words)-(29.6*number_of_sentences/number_of_words)-15.8

# Question 4: "Number of Syllables" in document
number_of_vowels = LSVD[2]
number_of_dipthongs = LSVD[3]
number_of_syllables = number_of_vowels - number_of_dipthongs

# Question 5: "Flesch-Kincaid score" of document (approximate grade level)
if number_of_sentences==0: #also try to prevent divide by zero errors
    number_of_sentences = 1
    print "POSSIBLE ERROR--attempted to divide by zero."
flesch_kincaid = (0.39*number_of_words/number_of_sentences)+(11.8*number_of_syllables/number_of_words)-15.59

# Output: Some of these are for debugging, may be removed in the future.
#print document_string
#print split_document_string
print "Analyzing the document" #+ str(input_file) + ":"
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

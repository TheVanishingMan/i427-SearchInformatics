# This file takes a document (preprocessed to make sure everything is on one line)
# then returns the document with all non-letters removed.

import os, sys

def process(ls):
    processed_list = []
    for word in ls:
        lower_word = word.lower()
        new_word = ''
        for character in lower_word:
            if character.isalpha():
                new_word = new_word + character
        processed_list.append(new_word)
    return ' '.join(processed_list)

input_file = sys.argv[1]
f = open(input_file, 'r')
document_string = f.read().splitlines()
split_document_string = document_string[0].split(" ")

#print split_document_string

# print the results to console so we can chain commands through bash.
print process(split_document_string)

f.close()

import os, sys

#our pre-processed training sets:
documents = ['business-words.txt', 'entertainment-words.txt', 'politics-words.txt', 'sport-words.txt', 'tech-words.txt']
for input_file in documents:
    f = open(input_file, 'r')
    write_to = documents.index(input_file)
    if write_to == 0:
        business_string = f.read().splitlines()
        split_business_string = business_string[0].split(" ")
    elif write_to == 1:
        entertainment_string = f.read().splitlines()
        split_entertainment_string = entertainment_string[0].split(" ")
    elif write_to == 2:
        politics_string = f.read().splitlines()
        split_politics_string = politics_string[0].split(" ")
    elif write_to == 3:
        sport_string = f.read().splitlines()
        split_sport_string = sport_string[0].split(" ")
    elif write_to == 4:
        tech_string = f.read().splitlines()
        split_tech_string = sport_string[0].split(" ")
    f.close()

command_argument_file = sys.argv[1]
f = open(command_argument_file, 'r')
input_document_string = f.read().splitlines()
input_document_list = input_document_string[0].split(" ")

# it might be redundent to check words that appear multiple times, consider a dictionary
#set_of_words_to_test = list(set(input_document_list))

#print input_document_list

#for word in set_of_words_to_test:
for word in input_document_list:
    #print split_tech_string
    print word
    tech_score = split_tech_string.count(word)
    sport_score = split_sport_string.count(word)
    business_score = split_business_string.count(word)
    entertainment_score = split_entertainment_string.count(word)
    politics_score = split_politics_string.count(word)
    
#    print "   tech          " + str(split_tech_string.count(word))
#    print "   sport         " + str(split_sport_string.count(word))
#    print "   business      " + str(split_business_string.count(word))
#    print "   entertainment " + str(split_entertainment_string.count(word))
#    print "   politics      " + str(split_politics_string.count(word))

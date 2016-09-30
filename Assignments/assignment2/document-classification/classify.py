import os, sys, math

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
        split_tech_string = tech_string[0].split(" ")
    f.close()

command_argument_file = sys.argv[1]
f = open(command_argument_file, 'r')
input_document_string = f.read().splitlines()
input_document_list = input_document_string[0].split(" ")

tech_category_score = 0
sport_category_score = 0
business_category_score = 0
entertainment_category_score = 0
politics_category_score = 0

for word in input_document_list:
    
    # count how many times the word appears in a certain type of document
    tech_score = split_tech_string.count(word)
    sport_score = split_sport_string.count(word)
    business_score = split_business_string.count(word)
    entertainment_score = split_entertainment_string.count(word)
    politics_score = split_politics_string.count(word)

    # calculate the logarithm of each of these scores (we don't want to log(0))
    if tech_score == 0:
        log_tech_score = 0
    else:
        log_tech_score = math.log(tech_score)
    if sport_score == 0:
        log_sport_score = 0
    else:
        log_sport_score = math.log(sport_score)
    if business_score == 0:
        log_business_score = 0
    else:
        log_business_score = math.log(business_score)
    if entertainment_score == 0:
        log_entertainment_score = 0
    else:
        log_entertainment_score = math.log(entertainment_score)
    if politics_score == 0:
        log_politics_score = 0
    else:
        log_politics_score = math.log(politics_score)
    
    #calculate the score for each category:
    tech_category_score = tech_category_score + log_tech_score - log_sport_score - log_business_score - log_entertainment_score - log_politics_score
    sport_category_score = sport_category_score + log_sport_score - log_business_score - log_entertainment_score - log_politics_score - log_tech_score
    business_category_score = business_category_score + log_business_score - log_entertainment_score - log_politics_score - log_tech_score - log_sport_score
    entertainment_category_score = entertainment_category_score + log_entertainment_score - log_politics_score - log_tech_score - log_sport_score - log_business_score
    politics_category_score = politics_category_score + log_politics_score - log_tech_score - log_sport_score - log_business_score - log_entertainment_score

category_scores = {}
category_scores[tuple('business')] = business_category_score
category_scores[tuple('entertainment')] = entertainment_category_score
category_scores[tuple('tech')] = tech_category_score
category_scores[tuple('sport')] = sport_category_score
category_scores[tuple('politics')] = politics_category_score

maxScore = max(category_scores.values())
mostLikely = ''.join(category_scores.keys()[category_scores.values().index(maxScore)])

print "Score for category:"
print " - business:      " + str(business_category_score)
print " - entertainment: " + str(entertainment_category_score)
print " - tech:          " + str(tech_category_score)
print " - sport          " + str(sport_category_score)
print " - politics:      " + str(politics_category_score)
print " "
print "The document's category is most likely: " + mostLikely

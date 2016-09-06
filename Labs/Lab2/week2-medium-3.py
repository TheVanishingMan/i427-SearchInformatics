# Enter your code here. Read input from STDIN. Print output to STDOUT
# Some inspiration came from a couple stackoverflow topics:
#       'get unique values from a list in python:'
#http://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python
#       'get all substrings of a list in python'
#http://stackoverflow.com/questions/22469997/how-to-get-all-the-contiguous-substrings-of-a-string-in-python


the_input_string = "BANANA"
#the_input_string = raw_input()

consonants = "BCDFGHJKLMNPQRSTVWXYZ"
vowels = "AEIOU"

stuart_substrings = [] #for book keeping
kevin_substrings = [] #refer to previous comment

def createSubstrings(input_word):
    string_length = len(input_word)
    return [input_word[i:j+1] for i in xrange(string_length) for j in xrange(i,string_length)]

permutations = createSubstrings(the_input_string)
#print permutations

def Minion(a_list, letter_set): #empty list (either stuart_substrings or kevin_substrings), consonants/vowels
    for word in permutations:
        if word[:1] in letter_set:
            a_list.append(word)
        else:
            continue
    #print a_list
    return a_list

stuart_length = len(Minion(stuart_substrings, consonants))
kevin_length = len(Minion(kevin_substrings, vowels))

#print stuart_length
#print kevin_length

if stuart_length > kevin_length:
    print "Stuart %d" % stuart_length
elif stuart_length < kevin_length:
    print "Kevin %d" % kevin_length
else:
    print "Draw"

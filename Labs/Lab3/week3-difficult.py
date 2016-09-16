# Question: Sherlock and the Valid String
# Link: https://www.hackerrank.com/challenges/sherlock-and-valid-string

# Enter your code here. Read input from STDIN. Print output to STDOUT

def valid(str): #takes an input as a string
    string_list = list(str) #'abcc' -> ['a','b','c','c']
    letters = list(set(string_list)) #unique letters in string_list
    occurrences = []
    for item in letters:
        occurrences.append(string_list.count(item))
    if len(list(set(occurrences))) == 1:
        return "YES"
    else:
        return "NO"

"""
The following two lines are removed in hackerrank, and the S=list(raw_input()) is uncommented
"""
S = list("aabbccdde") #sample code
print S #sample print


#S = list(raw_input()) #read the input
my_set = list(set(S)) #unique letters in the input (remove one at a time)
potential = []

potential.append(valid(''.join(S))) #test the original string

for item in my_set: #test each string with one letter removed
    test_string = ''.join(filter(lambda a: a !=item, S))
    potential.append(valid(test_string))

if 'YES' in potential: #the output, whether the string or substring is valid
    print "YES"
else:
    print "NO"

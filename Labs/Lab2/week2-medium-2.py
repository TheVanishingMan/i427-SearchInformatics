# The code is incomplete currently:
# Python/Strings/"Merge the Tools!"

# Enter your code here. Read input from STDIN. Print output to STDOUT
string = str(raw_input())
number = int(raw_input())
string_length = len(string)
substring_length = string_length/3


def removeDuplicates(input_string):
    occurred = []
    output = ""
    for letter in input_string:
        print letter
        print input_string
        if letter in occurred:
            input_string = input_string[1:]
        else:
            output = output + input_string[:1]
            occurred.append(input_string[:1])
            input_string[1:]
    print "OUTPUT:"
    print output
    return output

print "Remove Duplicates of AABBCC:"
print removeDuplicates("AABBCC")
#print " "

#print string[:number]
#string = string[:number]
'''

while string:
    sub = string[:number]
    print sub
    print ''.join(set(sub))
    string = string[number:]
'''

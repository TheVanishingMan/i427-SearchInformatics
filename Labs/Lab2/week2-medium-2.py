# The code is incomplete currently:
# Python/Strings/"Merge the Tools!"
# https://www.hackerrank.com/challenges/merge-the-tools

# Enter your code here. Read input from STDIN. Print output to STDOUT
#string = str(raw_input())
#number = int(raw_input())
string = "AABCAAADA"
number = 3

# Please note that these two lines have been changed to allow the code
# to work easier online.  Switching 'string' and 'number' to the two that
# are currently commented out will make the code function properly with raw_input()

string_length = len(string)
substring_length = number

def removeDuplicates(input_string):
    occurred = []
    output = ""
    for letter in input_string:
        if letter in occurred:
            input_string = input_string[1:]
        else:
            output = output + letter
            occurred.append(letter)
            intput_string = input_string[1:]
    return output

while string:
    sub = string[:substring_length]
    print removeDuplicates(sub)
    string = string[substring_length:]


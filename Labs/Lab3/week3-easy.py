# Question: Super Reduced String
# Link: https://www.hackerrank.com/challenges/reduced-string


# Enter your code here. Read input from STDIN. Print output to STDOUT
#string = list(raw_input())
# commented out to demonstrate
string = 'lrfkqyuqfjjfquyqkfrlkxyqvnrtyssytrnvqyxkfrzrmzlygffgylzmrzrfveulqfpdbhhbdpfqluevlqdqrrcrwddwrcrrqdql'
string = list(string)
#had a lot of issues at first because I was using ls.remove(ls[i])
#when I should have been using del ls[i]

def remove_adjacent_pair(ls):
    i = 0
    while i < len(ls)-1:
        if ls[i] == ls[i+1]:
            del ls[i]
            del ls[i]
            i = -1
        i = i + 1
    if not ls:
        return "Empty String"
    else:
        return ''.join(ls)

print remove_adjacent_pair(string)

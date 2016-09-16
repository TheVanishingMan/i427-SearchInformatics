# Question: Diwali Lights
# Link: https://www.hackerrank.com/challenges/diwali-lights

# Enter your code here. Read input from STDIN. Print output to STDOUT

"""
Commented out for demonstration
"""
#total = int(raw_input())
#tests = []
#while total:
#    tests.append(int(raw_input()))
#    total = total - 1

tests = [1,2,3,4,5,6,100]

def combinations(number_of_bulbs):
    output = 1
    i = 0
    while i < number_of_bulbs:
        output = output * 2
        output = output % 100000
        i = i + 1
    return output-1

for value in tests:
    print combinations(value)

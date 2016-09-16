# Question: Summing the N series
# Link: https://www.hackerrank.com/challenges/summing-the-n-series

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
Normally I would write the text cases for easy viewing. In this example
the formulas are run directly on the raw inputs though.
'''
total = int(raw_input())
while total:
    print ((int(raw_input()) ** 2) % 1000000007)
    total = total - 1

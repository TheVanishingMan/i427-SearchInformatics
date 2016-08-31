# Complete the function below.
# I cannot believe this problem was the followup to the matching parens problem.

def sum(numbers):
    output = 0
    for number in numbers:
        output = output + number
    return output

test = [1, 2, 3, 4, 5]
print "Should be 15"
print sum(test)
test2 = [12, 12]
print "Should be 24"
print sum(test2)

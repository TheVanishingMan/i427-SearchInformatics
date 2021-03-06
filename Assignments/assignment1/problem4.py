# As an added bonus, the presented solution uses tail recursion:

output = []

def cutSticks(lengths):
    if len(lengths) <= 1:
        return output
    else:
        output.append(len(lengths)-1)
        new_lengths = []
        minimum = min(lengths)
        for stick in lengths:
            if (stick - minimum) > 0:
                new_lengths.append(stick - minimum)
        return cutSticks(new_lengths)


'''     The above code works in this example, but seems to produce errors on hackerrank,
        I'm not sure why at the moment, but I suspect it has something to do with how the numbers
        are input into the function.


# As an added bonus, the presented solution uses tail recursion:
output = []

def cutSticks(lengths):
    if not lengths:
        return output
    else:
        output.append(len(lengths))
        new_lengths = []
        minimum = min(lengths)
        for stick in lengths:
            if (stick - minimum) > 0:
                new_lengths.append(stick - minimum)
        return cutSticks(new_lengths)
'''


test = [6, 5, 4, 4, 2, 2, 8]
print "Should be [6, 4, 2, 1]"
print cutSticks(test)
test2 = [8, 1, 2, 3, 4, 3, 3, 2, 1]
output = []
print "Should be [8, 6, 4, 1]"
print cutSticks(test2)

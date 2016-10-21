#!/usr/bin/env python2.7
import sys
import time as t

## Section 1: user input validation

routing_table = "road-segments.txt"
start_city = sys.argv[1]
end_city = sys.argv[2]
algorithm_choice = sys.argv[3]

print "Reading " + routing_table + " into a list."
with open(routing_table) as f:
    route_strings = f.readlines()
    route_list = []
    for string in route_strings:
        route_list.append(string.split())
print "\033[1;32mDone!\033[0m\n"

print "Begin at:  " + start_city
print "End at:    " + end_city
print "Algorithm: " + algorithm_choice

print "Making sure that the start_city and end_city are valid..."
found_start = False
found_end = False
route_list_length = len(route_list)
for i in range(0,route_list_length):
    if start_city in route_list[i]:
        found_start = True
        break
for i in range(0,route_list_length):
    if end_city in route_list[i]:
        found_end = True
        break

if not (found_start and found_end):
    print "\033[0;31mERROR! Invalid start city or end city.\033[0m"
    exit()
else:
    print "\033[1;32mValid!\033[0m\n"

## Section 2: algorithms

muttering_retreats = {}
def buildDictionary():
    for i in range(0, route_list_length):
        city_A = (route_list[i])[0]
        city_B = (route_list[i])[1]
        if muttering_retreats.has_key(city_A):
            if muttering_retreats[city_A] == None:
                muttering_retreats[city_A] = set([city_B])
            else:
                muttering_retreats[city_A].add(city_B)
        else:
            muttering_retreats[city_A] = set([city_B])
        if muttering_retreats.has_key(city_B):
            if muttering_retreats[city_B] == None:
                muttering_retreats[city_B] = set([city_A])
            else:
                muttering_retreats[city_B].add(city_A)
        else:
            muttering_retreats[city_B] = set([city_A])
        
buildDictionary()

#print muttering_retreats[start_city]
#print muttering_retreats[end_city]

def dfs(start, end):
    stack = [(start, [start])]
    while stack:
        #pop off the last element in the stack
        (city, route) = stack.pop()
        # explore each new city that has not been explored yet
        for next_city in (muttering_retreats[city] - set(route)):
            print len(route)
            if next_city == end:
                return route + [next_city]
            else:
                stack.append((next_city, route + [next_city]))

def bfs(start, end):
    queue = [(start, [start])]
    while queue:
        #pop off the first city in the queue
        (city, route) = queue.pop(0)
        for next_city in (muttering_retreats[city] - set(route)):
#            print len(route)
            if next_city == end:
                return route + [next_city]
            else:
                queue.append((next_city, route + [next_city]))

## Section 3: output

def pretty_print(city_list):
    total_road_segments = 0
    total_miles = 0.0
    for i in range(0, len(city_list)-1):
        city_A = city_list[i]
        city_B = city_list[i+1]
        for j in range(0, route_list_length):
            if (city_A in route_list[j]) and (city_B in route_list[j]):
                Street = (route_list[j])[3]
                miles = (route_list[j])[2]
                nextTown = city_B
                total_miles += float(miles)
                break
        print " - Take " + Street + " for " + str(int(miles) * 1.0) + " miles to " + nextTown
    print "\nTotal road segments: " + str(len(city_list)-1)
    print "Total distance: " + str(total_miles) + " miles"

if algorithm_choice == 'dfs':
    print "Depth-first search: (this either takes 1 second or 1 minute)"
    pretty_print (list((dfs(start_city, end_city))))
elif algorithm_choice == 'bfs':
    print "Breadth-first search (this took around 30-45 seconds on Tank):"
    pretty_print (list((bfs(start_city, end_city))))
else:
    print "\033[0;31mERROR! Invalid algorithm choice.\033[0m"

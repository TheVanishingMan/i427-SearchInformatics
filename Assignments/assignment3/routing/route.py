#!/usr/bin/env python2.7
"""
#python route.py [start-city] [end-city] [algorithm-choice: bfs, dfs, best]
print ' - Take IN_46 for 15.0 miles to Spencer,_Indiana'
print ' - Take US_231 for 6.0 miles to Romona,_Indiana'
Street = "US_231"
miles = 6.0
nextTown = "Romona,_Indiana"
print " - Take " + Street + " for " + str(miles) + " miles to " + nextTown
print '"Y"_City,_Arkansas Acorn,_Arkansas 15 US_71/270'
print '"Y"_City,_Arkansas Greenwood,_Arkansas 46 US_71'
print '"Y"_City,_Arkansas Hot_Springs,_Arkansas 70 US_270'
print 'Abbot_Village,_Maine Bingham,_Maine 24 ME_16'
print 'Abbot_Village,_Maine Guilford,_Maine 4 ME_6/15/16'
print 'Abbot_Village,_Maine Jackman_Station,_Maine 73 ME_6/15'
print 'Abbotsford,_Wisconsin Jct_WI_29_&_WI_97,_Wisconsin 12 WI_29'
print 'Abbotsford,_Wisconsin Marshfield,_Wisconsin 22 WI_13'
print 'Abbotsford,_Wisconsin Medford,_Wisconsin 14 WI_13'
print 'Abbotsford,_Wisconsin Withee,_Wisconsin 14 WI_29'
print 'Bloomington,_Indiana Spencer,_Indiana 15 IN_46'
print 'Romona,_Indiana Spencer,_Indiana 6 US_231'
print 'Spencer,_Indiana Terre_Haute,_Indiana 35 IN_46'
print 'Spencer,_Indiana Worthington,_Indiana 17 US_231'

"""

def dfs(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

print list(dfs(graph, 'C', 'F'))

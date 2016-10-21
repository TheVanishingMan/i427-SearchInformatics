#!/usr/bin/env python
import urllib2
import sys
import time as t
#from BeautifulSoup import BeautifulSoup as bs
from bs4 import BeautifulSoup as bs

seed = sys.argv[1] #http://www.cnn.com
maximum_pages = int(sys.argv[2]) #200
storage_dir = sys.argv[3] #pages/
algorithm = sys.argv[4] #dfs

url_dictionary = {}

def getPageLinks(target_url, document_number):
    url = target_url
    link = urllib2.urlopen(url)
    html = link.read()

    # if everything has worked correctly, we can add the html to a file:
    write_to_document = storage_dir + str(document_number) + '.html' #pages/5.html
    with open(write_to_document,"w") as wf:
        wf.write(html)
    with open('index.dat',"a") as wf:
        wf.write(str(document_number) + " " + url + "\n")

    url_dictionary[url] = set()

    soup = bs(html)
    for tag in soup.findAll('a', href=True):
        http_absolute_link_string = str(tag['href'])[:7]
        https_absolute_link_string = str(tag['href'])[:8]
        relative_link_1_string = str(tag['href'])[:1]
        relative_link_2_string = str(tag['href'])[:2]
        pdf_file_string = str(tag['href'])[-3:]
        if http_absolute_link_string == 'http://':
            if pdf_file_string != 'pdf':
                url_dictionary[url].add(tag['href'])
        elif https_absolute_link_string == 'https://':
            #url_dictionary[url].add(tag['href'])
            continue
        elif (relative_link_1_string == '/') and (relative_link_2_string != '//'):
            #url_dictionary[url].add(url + str(tag['href']))
            continue
        elif relative_link_2_string == '//':
            #url_dictionary[url].add('http:' + tag['href'])
            continue
            
def dfs(start):
    pages_explored = 0
    visited = set()
    stack = [start]
    while stack and (pages_explored < maximum_pages):
        url = stack.pop()
        if url not in visited:
            print "trying a page."
            try:
                getPageLinks(url, pages_explored)
                print str(pages_explored) + "/" + str(maximum_pages) + " " + url
#                print list(url_dictionary.keys())
                visited.add(url)
                stack.extend(url_dictionary[url] - visited)
                pages_explored = pages_explored + 1
            except urllib2.URLError, e:
                visited.add(url)
                print "\033[0;31mURL Error.\033[0m"
            except UnicodeEncodeError, e:
                visited.add(url)
                print "\033[0;31mUnicode Encoding Error.\033[0m"
    return visited

def bfs(start):
    pages_explored = 0
    visited = set()
    queue = [start]
    while queue and (pages_explored < maximum_pages):
        url = queue.pop(0)
        if url not in visited:
            try:
                getPageLinks(url, pages_explored)
                print str(pages_explored) + "/" + str(maximum_pages) + " " + url
#                print list(url_dictionary.keys())
                visited.add(url)
                queue.extend(url_dictionary[url] - visited)
                pages_explored = pages_explored + 1
            except urllib2.URLError, e:
                visited.add(url)
                print "\033[0;31mURL Error.\033[0m"
            except UnicodeEncodeError, e:
                visited.add(url)
                print "\033[0;31mUnicode Encoding Error.\033[0m"
    return visited

if algorithm == 'dfs':
    dfs(seed)
elif algorithm == 'bfs':
    bfs(seed)
else:
    print "\033[0;31mERROR! Invalid Algorithm choice.\033[0m"

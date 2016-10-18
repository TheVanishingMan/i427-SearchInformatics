# -*- coding: utf-8 -*-
from collections import deque
import scrapy


#===========
# Exceptions
#===========
class AlgoNotProvidedException(Exception):
    pass

class AlgoNotSupportedException(Exception):
    pass

class NumPageNotProvidedException(Exception):
    pass

class DestFolderNotProvidedException(Exception):
    pass

class UrlNotProvidedException(Exception):
    pass


#===========
# Containers
#===========
class Container(deque):
    ''' This is a class that serves as interface to the Spider '''
    def add_element(self, ele):
        ''' Add an element to the contain, always to the right '''
        return self.append(ele)

    def get_element(self):
        ''' This is an abstract method '''
        # One can also implement this using built-in module "abc",
        #   which stands for Abstract Base Class and produces a
        #   more meaningful error
        raise NotImplementedError

class Queue(Container):
    ''' Queue data structure implemented by deque '''
    def get_element(self):
        ''' Pop an element from the left '''
        return self.popleft()

class Stack(Container):
    ''' Stack data structure implemented by deque '''
    def get_element(self):
        ''' Pop an element from the right '''
        return self.pop()


#=======
# Spider
#=======
class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["example.com"]
    start_urls = (
        'http://www.example.com/',
    )

    def __init__(self, algo=None, num=None, directory=None, urls=None,
            *args, **kwargs):
        ''' Cutomized constructor that takes command line arguements '''
        super(ExampleSpider).__init__(*args, **kwargs)

        # check manditory inputs
        if num is None:
            raise NumPageNotProvidedException
        self.num_page_to_fetch = num

        if directory is None:
            raise DestFolderNotProvidedException
        self.dest_folder = directory

        if urls is None:
            raise UrlNotProvidedException
        self.start_urls = urls.split(',')

        # check algorithm choice, and construct container accordingly
        if algo is None:
            raise AlgoNotProvidedException
        elif algo == 'dfs':
            self.container = Stack()
        elif algo == 'bfs':
            self.container = Queue()
        else:
            raise AlgoNotSupportedException

        # TODO: if needed, add more initialization code below
        #
        return


    def parse(self, response):
        # TODO: Your job is to implement this function
        #
        # The following are accessible from self
        # - self.num_page_to_fetch = maximum number of pages to fetch
        # - self.dest_folder = path to folder where files should be stored
        # - self.container = Container object where urls are stored and extracted
        pass

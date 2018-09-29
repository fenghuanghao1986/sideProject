# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 11:06:19 2018

@author: fengh
"""

import scrapy

#must inherit from scrapy.Spider
class KittensSpider(scrapy.Spider):
    #can be any string, will be used to call from the console
    name = "kitten_getter"
    
    # This method must be in the spider, 
    # and will be automatically called by the crawl command.
    def start_requests(self):
        self.index = 0
        urls = [
            'http://reddit.com/r/cats',
        ]
        for url in urls:
            # We make a request to each url and call the parse function on the http response.
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        filename = "kitten_response"+str(self.index)
        with open(filename, 'wb') as f:
            #All we'll do is save the whole response as a huge text file.
            f.write(response.body)
        self.log('Saved file %s' % filename)
     
        
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 11:03:37 2018

@author: fengh
"""

#_*_coding:utf-8_*_
 
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    # add new URL to manager
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
 
    # add URLs to manager
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)
 
    # see if there is new URL in the manager
    def has_new_url(self):
        return len(self.new_urls) != 0
 
    # get new URL from the crawler
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
 

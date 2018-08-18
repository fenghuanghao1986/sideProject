# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 11:01:43 2018

@author: fengh
"""

#_*_coding:utf-8_*_
import urllib2
 
class HtmlDownloader(object):
 
    def download(self, url):
        if url is None:
            return None
 
        response = urllib2.urlopen(url)
 
        if response.getcode() != 200:
            return None
 
        return response.read()

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 11:04:05 2018

@author: fengh
"""

#_*_coding:utf-8_*_

import sys
sys.path.append("C:\Users\fengh\pythonProject\sideProject\web_crawler\baike_spider2")
print sys.path

import url_manager,html_downloader,html_parser,html_outputer
 
class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlPsrser()
        self.outputer = html_outputer.HtmlOutputer()
 
    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s'%(count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
 
                if count == 100:
                    break
                count = count + 1
 
            except:
                print 'craw fail'
 
        self.outputer.output_html()
 
 
if __name__=="__main__":
    # root page for crawler
    root_url = 'http://baike.baidu.com/item/Python'
    obj_spider = SpiderMain()
    # start crawler
    obj_spider.craw(root_url)

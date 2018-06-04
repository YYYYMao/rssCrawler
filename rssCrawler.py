#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import feedparser
import time

from config import * 
from pyquery import PyQuery as pq


class RssCrawler(object):
    
    def __init__(self):
        self.dataList = []


    def parseRss(self,rsslink):
        feed = feedparser.parse(rsslink)
        feed_entries = feed.entries
        for entry in feed.entries:
            obj = {}
            obj['title'] = entry.title
            obj['link'] = entry.link
            obj['description'] = entry.summary 
            obj['pubDate'] = int(time.mktime(entry.published_parsed)) if entry.published_parsed else int(time.mktime(time.strptime(entry.published, "%a,%d %b %Y %H:%M:%S %z"))) 
            obj['category'] = entry.category if hasattr(entry, 'category') else None
            html = self.getHTML(entry.link)
            obj['fullText'] = self.getFullText(html)
            self.dataList.append(obj)


    def getHTML(self,link):
        html = ''
        for keyword in crawlerKeyword :
            if keyword in link:
                if keyword == 'ftchinese' :
                    link = link + '?full=y'
                html = pq(url = link)(crawlerKeyword[keyword]).outerHtml()
                self.source = keyword
                break
        if html == '':
            html = pq(url = link).outerHtml()
            self.source = ''
        return html

    def getFullText(self,html):
        try : 
            text = stripHTML(html,self.source)
        except:
            text = ""    
        return text

        
if __name__ == "__main__":
    rsslink = 'http://www.chinatimes.com/rss/chinatimes-focus.xml'
    r = RssCrawler()
    r.parseRss(rsslink)
    print (r.dataList)
   

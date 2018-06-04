import re
from pyquery import PyQuery as pq

crawlerKeyword = {
    'chinatimes': '.arttext',
    'udn':'#story_body_content',
    'appledaily':'.ndArticle_margin',
    'cna':'.article_box',
    'reuters':'.body_1gnLA',
    'bnext':'.main_content',
    'nytimes':'.article-body',
    'ftchinese':'.story-body',
    'nikkei':'.newsText',
    'ltn':'div[itemprop="articleBody"]',
    'ettoday':'div[itemprop="articleBody"]',
    'epochtimes':'#artbody',
    'bbc':'.story-body__inner',
}

def stripHTML(html,source):
    if source == "chinatimes":
        html = pq(html).text()
        cleaner = re.compile('googletag.*}\);')
        cleantext = re.sub(cleaner, '', html)
        return cleantext
    elif source == "appledaily":
        html = pq(html).find('p').eq(0).remove('span,a').text()
        return html
    elif source == "cna":
        html = pq(html).find('p').eq(0).text()
        return html 
    elif source == "reuters":
        html = pq(html).remove('span,a').text()
        return html  
    elif source == "bnext":
        html = pq(html).remove('p:last').text()
        return html 
    elif source == "nytimes":
        html = pq(html).text()
        return html  
    elif source == "ftchinese":
        html = pq(html).remove('script').text()
        return html     
    elif source == "nikkei":
        html = pq(html).remove('script').find('p').text()
        return html  
    elif source == "udn":
        html = pq(html).remove('script ,style ,#story_bar, h1 ,h2 , #shareBar').text()
        return html 
    elif source == "ltn":
        html = pq(html).remove('script ,style ').text()
        return html 
    elif source == "ettoday":
        html = pq(html).remove('script ,style ').text()
        return html  
    elif source == "epochtimes":
        html = pq(html).remove('script ,style ').find('p').text()
        return html    
    elif source == "bbc":
        html = pq(html).remove('script ,style ').find('p').text()
        return html                               


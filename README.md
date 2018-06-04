# rssCrawler
crawl news from main website

rss list
* 聯合新聞網
* 路透社
* 中時
* 蘋果日報
* 中央社
* 日經
* 紐約時報
* 金融時報
* 數位時代
* 自由時報
* 大紀元
* ettoday
* BBC中文網

How to use 
```python
rsslink = 'http://www.chinatimes.com/rss/chinatimes-focus.xml'
r = RssCrawler()
r.parseRss(rsslink)
print (r.dataList)
```

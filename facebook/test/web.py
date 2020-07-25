import urllib2
import re

HREF_REGEX = "href=['\"https://]+[a-zA-Z]+\.[a-zA-Z]+\.[a-zA-Z]+"
site = "www.facebook.com"
request = urllib2.Request(site, headers={})
page = urllib2.urlopen(request)
html = page.read()
crawled_urls, tobe_crawled_urls = list(),list()

for link in re.findall(HREF_REGEX,html):
    if url is not in line.strip('href=')[1:]):
        tobe_crawled_urls.append(url)


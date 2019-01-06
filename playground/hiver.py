import urllib2

response = urllib2.urlopen("https://hiverhq.com")
page_source = response.read()
print(page_source)

import urllib2

req = urllib2.Request(site, headers)

try:
    page = urllib2.urlopen(req)
except err:
    print(err)

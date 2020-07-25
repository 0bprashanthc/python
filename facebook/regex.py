import re
import urllib2

req = urllib2.Request("www.google.com", headers={})
page = urllib2.urlopen(req)

regex = re.compile("<.*?>")

text = """<div>
<h1>Title</h1>
<p>A long text........ </p>
<a href=""> a link </a>
</div>"""

text = regex.sub("",text)
page = regex.sub("",page)
print(text)
print(page)

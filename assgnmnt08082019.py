import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = input ('Enter count:')
count = int(count)
position = input ('Enter position:')
position = int(position) - 1 
n = 0
while n < count:
    n = n + 1
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    taglist = list()
    tags = soup('a')
    for tag in tags:
        tag = tag.get('href', None)
        taglist.append(tag)
    url = taglist[position]
    print(url)

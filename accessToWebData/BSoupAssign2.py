import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html,'html.parser')

for i in range(0,7) :
    # Retrieve all of the anchor tags
    tags = soup('a')
    # 3rd tag reference
    tag3 = 0
    for tag in tags:
        tag3 += 1
        if tag3 == 18 :
            ftag = tag.get('href', None)
            print(tag.contents[0])
            #print(ftag)
    html = urllib.request.urlopen(ftag, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

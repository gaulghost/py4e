from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
#import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
fsum = 0
tags = soup('span')
for tag in tags:
    #fnum = re.findall('.+>([0-9]+)<.+',tag)
    #fsum = fsum + int(fnum)
    fsum = fsum + int(tag.contents[0])
print(fsum)

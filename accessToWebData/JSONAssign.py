import json
import ssl
import urllib.request , urllib.parse , urllib.error

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL :- ')
fh = urllib.request.urlopen(url , context=ctx ).read()

sum = 0
info = json.loads(fh)
info1 = info['comments']
for item in info1:
    print('count', item['count'])
    sum = sum + int(item['count'])
print("===========SUM===========")
print(sum)

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
print(data.decode())
tree = ET.fromstring(data)

sum = 0
counts =  tree.findall('comments/comment')
print('User Count: ' , len(counts))
for cnt in counts :
    num = cnt.find('count').text
    sum = sum + int(num)
print('Sum of count is :' , sum)

#countsss = tree.findall('.//count')

#print(counts)

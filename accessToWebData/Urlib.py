import urllib.request , urllib.parse , urllib.error

fhand = urllib.request.urlopen('http://ugadmissions.iiit.ac.in/leee_page.html#')

for fline in fhand :
    print(fline.decode().rstrip())

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
print("Enter URL: http://py4e-data.dr-chuck.net/known_by_Jarell.html")
url =  'http://py4e-data.dr-chuck.net/known_by_Jarell.html'
#html = urllib.request.urlopen(url, context=ctx).read()
#soup = BeautifulSoup(html, 'html.parser')

count = 0

while count < 7:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    pos = 1
    tags = soup('a')
    for tag in tags:
        if pos == 18:
            url = tag.get('href', None)
            break
        else:
            pos += 1
    count += 1

#print(url)
    
word = url.split('_')[2]
name = word.split('.')[0]
print (name)

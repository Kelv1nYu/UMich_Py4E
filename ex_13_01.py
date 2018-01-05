import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_55437.xml'
data = urllib.request.urlopen(url).read()

#print(data)

tree = ET.fromstring(data)

counts = tree.findall('.//count')

tot = 0

for item in counts:
    #print(item.text)
    tot = tot + int(item.text)

print(tot)

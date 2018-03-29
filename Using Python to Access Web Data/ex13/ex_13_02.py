# json
import json
import urllib.request, urllib.parse, urllib.error

url = 'http://py4e-data.dr-chuck.net/comments_55438.json'

data = urllib.request.urlopen(url).read()

info = json.loads(data)

tot = 0
for item in info['comments']:
    #print(item['count'])
    tot = tot + int(item['count'])

print(tot)

# You are to look through all the <comment> tags and find the <count> values sum the numbers. 
# To make the code a little simpler, you can use an XPath selector string to look through the entire tree of XML 
# for any tag named 'count' with the following line of code:
# counts = et.findall('.//count')

import xml.etree.ElementTree as et
import urllib.parse, urllib.request, urllib.error

URL = 'https://py4e-data.dr-chuck.net/comments_1912338.xml'
count = 0
sum = 0

uh = urllib.request.urlopen(URL)
data = uh.read()
print('Retrieved', len(data), 'characters')
print(data.decode())
tree = et.fromstring(data)
results = tree.findall('comments/comment')
for i,j in enumerate(results):
    count = results[i].find('count').text
    sum = int(count) + sum
print(sum)

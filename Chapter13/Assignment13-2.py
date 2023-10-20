# The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, 
# compute the sum of the numbers in the file and enter the sum below:

import json
import urllib.parse, urllib.request, urllib.error, urllib.response

URL = 'http://py4e-data.dr-chuck.net/comments_1912339.json'
sum = 0

uh = urllib.request.urlopen(URL)
data = uh.read().decode()
json_data = json.loads(data)
for i in json_data['comments']:
    value = i['count']
    sum = value + sum
print(sum)
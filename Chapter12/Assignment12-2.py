import urllib.request, urllib.parse, urllib.error, urllib.response, urllib.robotparser
from bs4 import BeautifulSoup
import ssl
import re

fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1912336.html')
soup = BeautifulSoup(fhand, 'html.parser')

spans = soup('span')
sum = 0
for span in spans:
    num = int(span.contents[0])
    sum = num + sum
print(sum)
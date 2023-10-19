# In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. 
# The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, 
# scan for a tag that is in a particular position relative to the first name in the list, 
# follow that link and repeat the process a number of times and report the last name you find.

# Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Aleisha.html
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is E:
# Strategy
# The web pages tweak the height between the links and hide the page after a few seconds to make it difficult 
# for you to do the assignment without writing a Python program. But frankly with a little effort and 
# patience you can overcome these attempts to make it a little harder to complete the assignment 
# without writing a Python program. But that is not the point. The point is to write a clever Python program to solve the program.

import urllib.request, urllib.parse, urllib.error, urllib.response, urllib.robotparser
from bs4 import BeautifulSoup
import ssl
import re

URL = 'http://py4e-data.dr-chuck.net/known_by_Aleisha.html'


count = 7
current_count = 0
pos = 18
while current_count < count:
    html = urllib.request.urlopen(URL)
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for i, tag in enumerate(tags):
        if i == pos - 1:
            URL = tag.get('href', None)
            name = tag.contents[0]
            break
        else:
            continue

    current_count += 1

print('last url: ', URL)
print ('name = ', name)



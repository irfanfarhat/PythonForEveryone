# Assignment 10.2 
# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, 
# print out the counts, sorted by hour as shown below.

file = open('mbox-short.txt')
hr = dict()
for line in file:
    lines = line.rstrip()
    if lines.startswith('From'):
        words = lines.split()
        if len(words) >= 6:
            time = words[5]
            hour = time.split(':')[0]
            hr[hour] = hr.get(hour, 0) + 1

shr = sorted(hr.items())
for hour, count in shr:
    print(hour, count)
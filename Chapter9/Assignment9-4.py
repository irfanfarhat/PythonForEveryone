# Assignment 9.4 
# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

file = open('mbox-short.txt')
emails = dict()

for line in file:
    line = line.rstrip() #strip here is not really needed as we are already doing split which gives each word separately
    if line.startswith('From'):
        words = line.split()

        if len(words) > 3:
            if words[1] not in emails:
                emails[words[1]] = 1
            else:
                emails[words[1]] = emails[words[1]] + 1
            # The below line of code with get will replace the if else statement.
            # for word in words:
            #   emails[word] = emails.get(word,0) + 1 
big = None
max = None
for key,value in emails.items():
    if max is None or value > max:
        big = key
        max = value

print(big, max)

x = {'chuck' : 1, 'fred': 3}
y = x.items()
print(y)
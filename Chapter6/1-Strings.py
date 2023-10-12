# This program will count number of times a letter is repeated in a string
# Example how many a are in banana

word = input('enter the word')
ch = input('enter the character to count')
count = 0
for iterate in word:
    if iterate == ch:
        count = count + 1

print('the character', ch, ' is repeated ', count, ' times in ', word  )



import re
sum = 0
file = open('regex_sum_1912334.txt')

content = file.read()
integers = re.findall('[0-9]+', content)
for i in integers:
    num = int(i)
    sum = sum + num

print('sum = ', sum)
    

# To find whether a line/word start with specific word/character, there is a method for that too
# startwith(): it can be used for this purpose, it is a logical method and return True or False
# it require one parameter and it will be used for searching

line = 'Hello! I hope you are learning Python'

startingwith = line.startswith('Hello!')
print(startingwith)

swith = line.startswith('H')
print(swith)

stwith = line.startswith('h')
print(stwith)

srwith = line.startswith('Hel')
print(srwith)
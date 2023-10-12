# replace(): This method will replace all occurances of the search string with the replacement string.
# This also creates a copy so it needs to be stored separately.
# replace() is more like search and replace. This method require two parameters
# First: what you want to search, Second: what you want to replace it with

word = 'Hello World!'
print(word)
newword = word.replace('World!', 'There!')
print(newword)

# replace() can also be used to replace specific characters and not just words

word2 = word.replace('l', 'o')
print(word2)

word3 = word.replace('l', 'xyz')
print(word3)


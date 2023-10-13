# Dictioonary is another mutable data structure in Python. Mutable means we can make changes to the Dictionary.
# Dictionaries store key-value pairs.
# They are used for fast data retrieval based on keys.
# Keys must be unique, and dictionaries are unordered.
# bag = {'money' : 2000, 'books' : 4, 'pen' : 5}
# bag = name of dictionary, money, books, pen are keys, 2000, 4, 5 are values for the keys respectively, keys are labels basically

bag = {'money' : 2000, 'books' : 4, 'pen' : 5}
print(bag)

# updating values, we need to provide a key and add new value to it on the right side and store it in the left side.
bag['books'] = bag['books'] + 10
print(bag)
bag['pen'] = 10
print(bag)

# we can also create new dictionary with contructor dict(), the order is not same so don't expect that.

pack = dict()
pack['item1'] = 5
pack['item2'] = 43
pack['keys'] = 3
print(pack)

# we can do this as well, remember that 23 is the key and 'irfan' is the value. we provide keys in brackets
pack['23'] = 'irfan'
print(pack)
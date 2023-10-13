# List is one of the data structure in Python, Data structures provide a way to efficiently store, retrieve, and manipulate data
# List is a collection allows us to put many values in one variable
# with normal variables we are storing only one value like name = 'bob' but List allow us to store more than one value in one variable.
# List are mutable means we can make changes to the list using the index


# name is a list, List has square brackets (this is important), name1, name2, name3 are values, index start with 0, 
# At index 0 is name1, index 1 is name2, index 3 is name. Index are used for accessing values.
name = ['name1','name2', 'name3']
print(name[1]) # access item no 1 (which is name2) in name list.

# the data doesn't have to be the same
items = ['string', 34, 67.0]
print(items[2])

# You can have a nested list (Inception), At index 1 for nestedlist is another list
nestedlist = [1, ['item', 3.0], 'value']
print(nestedlist[1])

# To access items nested : this will output 'item' as that is the 0 index item in nestedlist
# [1] for the index 1 item in nestedlist, this will be nested list ['item', 3.0]
# [0] for accessing the 0 index item in nested list 
print(nestedlist[1][0]) 



#Changing list using index
name[1] = 'bob' # this will replace name2 with bob in the list created above name = ['name1', 'name2', 'name3']
print(name[1])

# making chanes to the nested list
# nestedlist = [1, ['item', 3.0], 'value'] this is already created above.

nestedlist[1][1] = 'item2'
print(nestedlist[1])
print(nestedlist[1][1])



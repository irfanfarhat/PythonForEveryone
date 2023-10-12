# upper(): This will convert the string to upper case but it must be stored in separate
# copy as lower creates a duplicate

letter = 'this has no capital letters'

#since upper() will create a duplicate, assinging it to Lletter for output
Cletter = letter.upper()
print(Cletter)

#the following will work but can't output as it is not stored anywhere
#  letter.upper()
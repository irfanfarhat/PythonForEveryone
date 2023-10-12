# strip(): This method will remove white spaces, a white space is a blank space but some other characters also count as whitespace.
# strip has three variants, lstrip(): remove white space on the left side.
# rstrip(): remove white space on the right side, strip(): remove on both sides. None of them remove whitespace in the middle.
# it also create another copy and need to be stored somewhere

word = '   Hello There    '
sword = word.strip()
print(sword)
lword = word.lstrip()
print(lword)
rword = word.rstrip()
print(rword)
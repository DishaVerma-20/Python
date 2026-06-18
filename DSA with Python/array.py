import array as arr

val = arr.array('i', [1,2,3,4,5,6])
print(val)

for i in range(0,6):
    # print(val[i])
    print(val[i], end = ' ')

    # sep delimiter/separator ka kaam karta hai.
    # end line ke end me kya add karna hai, uske liye hota hai.

print('\n') # Backward slash


# enhanced for loop hai yeh, directly acccessing elements without index
for x in val:
    print(x, end = ' , ')


# another approach for array
# from array import *
# yha hame no need of writing module array 
# val = array('i', [....])

print('\n')

# we can use len function too
for i in range(0, len(val)):
    print(i)


# for identifying the typecode of array
print(val.typecode)

# Reverse the elements of array
print(val.reverse()) # it will return none

for x in val:
    print(x, end = ' ')

# python mai kuch methods object ko modify krte hai aur phir none return krte hai print krne pr

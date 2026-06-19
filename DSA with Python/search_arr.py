from array import *
arr = array('i', [10, 20, 30, 40, 50, 60, 70])
a = arr.index(60)
print(a)
print(arr.index(100)) # ValueError: x not in array

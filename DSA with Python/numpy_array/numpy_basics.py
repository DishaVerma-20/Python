from numpy import *
# import numpy as np 

val = array([1,3,6,9,12])

for x in val:
    print(x, end = ' ')

# import numpy as np
# print(np.__version__)

print('\n')
val = array([1,3,6,9.5,12]) # type casting use krega
# sab float mai convert ho jaayge
for x in val:
    print(x, end = ' ')


print('\n')

val = array([1,3,6,9.4,12,'a'])
# 1 char aa gaya toh ab yeh heterogeneous data hai, yha yeh unicode consider hogaa..
for x in val:
    print(x, end = ' ')
print(val.dtype) # unicode 32 is type


print('\n')
# type specify krke
val = array([1,3,6,9,12], float)

for x in val:
    print(x, end = ' ')

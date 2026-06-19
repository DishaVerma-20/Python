from array import *

arr = array('i', [1,2,3,4,5,6,7,8,9])
for x in arr:
    print(x, end = ' ')
print('\n')

# arr1 = arr[start index : end index]
arr1 = arr[2:7]
for x in range(0, len(arr1)):
    print(arr1[x], end = ' ')
print('\n')

# ab mujhe index nahi pata and mereko last ke 3 elements nahi chahiye, thenn..
arr1 = arr[2:-3]
for x in range(0, len(arr1)):
    print(arr1[x], end = ' ')

print('\n')
# now we want to reverse the elements of array without using reverse , so we use array slicing
rev = arr[::-1]
for x in rev:
    print(x, end = ' ')
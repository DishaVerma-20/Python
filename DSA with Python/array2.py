from array import *
arr = array('i', [1,2,3,4,5,6,7,8])
arr.insert(1, 50) # this is for inserting elements
arr.append(100) # inserting elements at last
arr[2] = 12456 # replacing the existing element
for x in arr:
    print(x, end = ' ')

print('\n')

arr = array('i', [1,2,3,4,5,6,7,8])
for x in arr:
    print(x, end = ' ')

print('\n')

copyArray = array(arr.typecode, (x*2 for x in arr))# generator
# copyArray = array(arr.typecode, (x*4 for x in arr))

copyArray.pop(3) # 3 is index here

for x in range(0, len(copyArray)):
    print(copyArray[x], end = " ")


# When we do not know the index, toh hum element delete krne ke liye remove ka use krege
copyArray.remove(12)

print('\n')
for x in range(0, len(copyArray)):
    print(copyArray[x], end = " ")
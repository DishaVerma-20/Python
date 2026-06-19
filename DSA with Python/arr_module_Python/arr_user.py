from array import *

arr = array('i', [])

n = int(input("Enter how many numbers in array? "))
for i in range (0, n):
    arr.append(int(input("Enter number:- ")))

for i in range(0, len(arr)):
    print(arr[i], end = ' ')
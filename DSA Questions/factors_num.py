# num = int(input())
# for i in range (1, num+1):
#     if num % i == 0:
#         print(i, end = ' ')


# num = int(input())
# result = []
# for i in range (1, num + 1):
#     if num%i == 0:
#         result.append(i)
# print(result)


# better solution
# num = int(input())
# result = []
# for i in range (1, num//2):
#     if num%i==0:
#         result.append(i)
# result.append(num)
# print(result)

from math import *
# Optimal solution
num = int(input())
result = []
for i in range(1, int(sqrt(num))+1):
    if num % i == 0:
        result.append(i)
        if num//i != i:
            factor = num //i
            result.append(factor)
print(result)
result.sort()
print(result)


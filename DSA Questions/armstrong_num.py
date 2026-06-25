from math import *
n = int(input())

num = n
count = int(log10(n) + 1)
sum = 0

while num>0:
    last_digit = num % 10
    num = num//10
    # count = count + 1
    sum = sum + last_digit**count

print(count)
print(n==sum)
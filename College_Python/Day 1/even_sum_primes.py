import math
A = int(input())
B = int(input())

def digit_sum(num):
    sums = 0
    while num>0:
        mod = num % 10
        sums = sums + mod
        num = num // 10
    return sums

def prime(num):
    if num<2:
        return True
    sqrts = int(math.sqrt(num))
    for i in range (2, sqrts+1):
        if (num%i==0):
            return False
    return True
count = 0
for i in range (A, B+1):
    
    if prime(i):
        if digit_sum(i)%2 == 0:
            count += 1
print(count)

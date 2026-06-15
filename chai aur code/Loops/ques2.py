# Sum of even numbers
# Problem: Calculate the sum of even numbers up to a given number n. 
n = int(input())
sums = 0
for i in range(n):
    if (i %2==0):
        sums = sums + i

print(sums)
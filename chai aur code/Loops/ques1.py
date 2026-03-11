# Counting positive numbers
# Problem: Given a list of numbers, count how many are positive.
# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
count = 0
for i in numbers:
    if i > 0: 
        count+=1
print(count)

# syntax of list comprehension
# [expression for item in iterable]
# numbers = [int(x) for x in input("Enter numbers: ").split()]
# ya frr
# list_num = list(map(int, input().split())) 

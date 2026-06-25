num = int(input())

count = 0

while num>0:
    last_digit = num % 10
    num = num // 10
    count = count + 1

print(count)
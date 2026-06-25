n = int(input())

num = n
result = 0

while num > 0:
    last_digit = num % 10
    num = num // 10
    result = result * 10 + last_digit

print(result)

print(n==result)


    
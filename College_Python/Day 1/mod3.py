start = int(input())
end = int(input())
count = 0

for i in range(start, end+1):
    if (i%3 == 0):
        temp = i
        sum = 0
        while(temp>0):
            mod = temp % 10
            sum = sum + mod
            temp = temp // 10
        if (sum % 2 == 0):
            count += 1
print(count)

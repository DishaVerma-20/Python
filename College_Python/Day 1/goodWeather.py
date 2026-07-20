# a1, a2, a3, a4, a5, a6, a7 = map(int, input().split())

count_0 = 0
count_1 = 0

for i in range(0, 7):
    ip = int(input())
    if ip == 1:
        count_1 += 1
    else:
        count_0 += 0

if count_0<count_1:
    print("YES")
else:
    print("NO")
    

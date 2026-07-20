d, x, y, z = map(int, input().split())
work1 = 7 * x
rem = 7-d
work2 = (y * d) + (z * rem)
if work1>work2:
    print(work1)
else:
    print(work2)
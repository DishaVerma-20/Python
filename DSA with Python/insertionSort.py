def insertionSort(a):
    n = len(a)

    for i in range (1, n):
        key = a[i]
        j = i-1
        while(j>=0 and key<a[j]):
            a[j+1] = a[j]
            j = j-1

        a[j+1] = key

a = [56, 23, 45, 40, 69, 78, 2, 51]
insertionSort(a)
print(a)
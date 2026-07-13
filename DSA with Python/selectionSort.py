# Selection sort
def selectionSort(a):
    n = len(a)

    for i in range(n):
        min = i
        for j in range (i, n):
            if a[min]>a[j]:
                min = j
        a[i], a[min]= a[min], a[i]

a = [56, 78, 23, 45, 40, 69, 78, 2, 51]
selectionSort(a)
print(a)

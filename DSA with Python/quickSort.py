def quickSort(arr, l ,r):
    if l<r: # base condn for recursion, no interchange, otherwise overlap
        p = partition(arr, l, r)

        quickSort(arr, l, p-1)
        quickSort(arr, p+1, r)

def partition(arr, l, r):
    pivot = arr[l]
    i = l+1
    j = r

    while True: # infinite loop and also no condition check
        while (i<=j and arr[i]<pivot):
            i = i+1

        while (i<=j and arr[j]>pivot):
            j = j-1

        if (i<j): # dusri condition false haiii
            arr[i], arr[j] = arr[j], arr[i]
        else:
            # i > j hai aur i = j ho gaya hai toh dono case mai break
            break
    
    arr[l], arr[j] = arr[j], arr[l]
    return j

arr = [23, 45, 12, 65, 34, 10, 3]
quickSort(arr, 0, len(arr)-1)
print(arr)
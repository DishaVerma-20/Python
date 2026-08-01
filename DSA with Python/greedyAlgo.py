def max_min_diff(arr):
    arr.sort() # function hai yeh
    # phir find the length of arr 
    n = len(arr)
    mid = n//2 # integer division
    max = 0
    min = 0
    j = len(arr) - 1

    for i in range(mid):
        max = max + abs(arr[i]-arr[j])
        j = j-1

        min = min + abs(arr[2*i] - arr[2*i+1])

    print(f"Maximum difference is {max}")
    print(f"Minimum difference is {min}")

arr = [12, 5, 25, 10, 2, 15, 8, 30]
max_min_diff(arr)

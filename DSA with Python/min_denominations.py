def min_denominations(arr):
    arr.sort(reverse = True)
    n = len(arr)
    amt = int(input("Enter the amount: "))
    count = 0

    for j in range(n):
        while arr[j]<=amt:
            amt = amt-arr[j]
            count += 1
    print(count)

arr = [1, 2, 5, 200, 100, 10]
min_denominations(arr)


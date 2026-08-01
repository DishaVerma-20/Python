# Find minimum and maximum element in an array.
def find_min_max(arr, start, end):

    # for 1 element only
    if (start == end):
        # Base condition
        return arr[start], arr[end] # tuple bnakr bhej dega
    # Base condition hogi, hamare array mai 1 he element hai ya phir hmare array mai 2 element haiii

    # 2 elements
    if (start + 1 == end):
        if arr[start]<arr[end]:
            return arr[start], arr[end]
        # assuming phli value is minimum and dusri value is maximum
        else:
            return arr[end], arr[start]

    # mid index find krte haii
    # integer division
    mid = (start + end) // 2

    min1, max1 = find_min_max(arr, start, mid)
    min2, max2 = find_min_max(arr, mid+1, end)

    return min(min1,min2), max(max1, max2)

arr = [23, 14, 45, 3, 6, 10]
min, max = find_min_max(arr, 0, len(arr)-1)
print("Minimum value is ", min)
print("Maximum value is ", max)

        

"""
Given a **sorted** array arr[] of length n, modify the array in‑place so that all distinct values appear at the beginning of the array while preserving their original order. After the distinct segment, the remaining positions may contain any values and are irrelevant for the result.

The function should return the length of the prefix that contains the unique elements.

### Example
Input:  arr = [2, 2, 2, 2, 2]
Output: 1
Modified array (first part): [2]

All elements are identical, so only one* `2` *is kept.
"""

class Solution:
    def uniqueSortedElements(self, arr):
        n = len(arr)
        # two pointer approach

        # check khali toh nahi hai array
        if n == 0:
            return 0

        j = 1

        for i in range(1, n):
            if arr[i] != arr[i-1]: # unique element
                arr[j] = arr[i]
                # agar unique elemnt hai toh koi chng nhi, frst iter mai i, j dono 1 haii
                j += 1

        return j

arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
sol = Solution()
print(sol.uniqueSortedElements(arr))
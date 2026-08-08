"""
Given an integer array `arr`, determine whether the elements are arranged in non‑decreasing order (each element is **less than or equal to** the next one). Equal values are allowed, and any pair of consecutive equal values is considered sorted. Return `true` if the entire array satisfies this condition; otherwise, return `false`.

# Example 1
Input: arr = [5, 12, 12, 20, 35]
Output: true
Explanation: Every element is less than or equal to the one that follows, so the array is sorted.


"""

class Solution:
    def isAscending(self, arr):
        n = len(arr)
        # small = arr[0]
        # for i in range(0, n+1):
        #     if n == 1:
        #         return True
        #     if arr[i]<=small and arr[i]<=arr[i+1]:
        #         small = arr[i]
        #         return True
        #     else:
        #         return False
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                return False
        return True

arr = [5, 12, 12, 20, 35]
sol = Solution()
print(sol.isAscending(arr))
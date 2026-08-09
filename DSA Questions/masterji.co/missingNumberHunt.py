"""
Given an integer array **arr** of length *n-1* that contains **distinct** numbers taken from the range **\[1, n\]**, exactly one number from this range is absent. The task is to identify and return the missing integer.

**Input**: An array `arr` of size `n-1` with distinct values, each between `1` and `n` inclusive.
**Output**: The single integer from `1` to `n` that does not appear in `arr`.
Input: arr = [5, 1, 3, 4]
Output: 2
Explanation: The numbers should be 1 through 5. The array lacks the value 2, so the answer is 2.

"""

class Solution:
    def findMissingNumber(self, arr):
        n = len(arr) + 1
        # arr.sort()
        # if (len(arr) == 0) or arr[0] != 1 :
        #     return 1
        # for i in range(0, n-2):
        #     j = arr[i] + 1
        #     if j != arr[i+1]:
        #         return j 
        # return n

        # for i in range(1, n+1):
        #     if i not in arr:
        #         return i

        expected_sum = (n * (n+1)) // 2
        sum = 0
        for i in arr:
            sum = sum + i
        return expected_sum-sum
            
arr = [5, 1, 3, 4]
sol = Solution()
print(sol.findMissingNumber(arr))
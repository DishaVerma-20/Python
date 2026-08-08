"""
Given an integer array `arr`, rearrange the elements so that every occurrence of `0` is shifted to the end of the array. The relative order of all non‑zero elements must remain unchanged.

Input: arr = [1, 2, 0, 4, 3, 0, 5, 0]
Output: [1, 2, 4, 3, 5, 0, 0, 0]
*Explanation*: The three zeros are moved after all other numbers while the order `1, 2, 4, 3, 5` stays the same.

"""
class Solution:
    def shiftZerosToEnd(self, arr):
        n = len(arr)
        j = 0
        # for i in range(n-1):
        #     if arr[i] == 0:
        #         while arr[j] == 0 and i<j:
        #             j -= 1
        #     if i<j:
        #         arr[i], arr[j] = arr[j], arr[i]
        # return arr
        # wronggg

        for i in range (n):
            if arr[i]!=0:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
        return arr

arr = [1, 2, 0, 4, 3, 0, 5, 0]
sol = Solution()
print(sol.shiftZerosToEnd(arr))

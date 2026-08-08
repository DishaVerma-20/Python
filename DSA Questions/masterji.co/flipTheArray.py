"""
Reverse the given array `arr[]`. Reversing an array means rearranging its elements so that the first element becomes the last, the second element becomes the second‑last, and so on.
```
Input: arr[] = [1, 4, 3, 2, 6, 5]
Output: [5, 6, 2, 3, 4, 1]
Explanation: The element `1` moves to the last position, `4` moves to the second‑last, etc.
```
"""
class Solution:
    def flipArray(self, arr):
        n = len(arr)
        j = n - 1
        for i in range (n):
            if j > i:
                arr[i], arr[j] = arr[j], arr[i]
                j -= 1
        return arr
arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
sol = Solution()
print(sol.flipArray(arr))
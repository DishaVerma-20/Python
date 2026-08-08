'''Given an array arr of length n, identify all *leaders* in the array. An element is called a leader if it is greater than or equal to every element that appears to its right. The rightmost element is always a leader because there are no elements after it.

Input: An array `arr[]`.

Output: A list of all leaders in the order they appear in the array.

### Example 1
Input: arr = [16, 17, 4, 3, 5, 2]
Output: [17, 5, 2]
Explanation: 17 is greater than all elements to its right [4, 3, 5, 2]; 5 is greater than the element to its right [2]; 2 has no elements to its right.'''

class Solution:
    def findLeaders(self, arr):
        """
        Finds all right-side leaders in the given array.
        :param arr: List[int] - The input array of integers.
        :return: List[int] - Leaders in the order they appear.
        """
        # Your implementation here
        n = len(arr)
        leaders = []

        max_right = arr[n-1]
        leaders.append(arr[n-1])

        for i in range(n-2, -1, -1):
            if arr[i]>=max_right:
                leaders.append(arr[i])
                max_right = arr [i]

        leaders.reverse()
        return leaders
    
arr = [16, 17, 4, 3, 5, 2]
sol = Solution()
res = sol.findLeaders(arr)
print(res)

"""
Given the head of a singly linked list, return the middle node of the list.

- If the list contains an odd number of nodes, there is a single middle node; return that node.
- If the list contains an even number of nodes, there are two middle nodes; return the second one (the one that appears later in the list).

```
Input: 1 → 2 → 3 → 4 → 5
Output: Node with value 3
Explanation: The list has 5 nodes, so the middle node is the 3rd node, which holds the value 3.
```

```
Input: 10 → 20 → 30 → 40 → 50 → 60
Output: Node with value 40
Explanation: The list has 6 nodes. The two middle nodes are 30 and 40; according to the rule we return the second middle node, which holds the value 40.
```

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        count = 0
        curr = head
        t1 = head
        # t1 = head.ext if count = 1
        while t1:
            count += 1
            t1 = t1.next
        if count%2 == 0:
            mid = ((1+count)//2)+1
        else:
            mid = (1+count)//2

        count = 1
        while curr:
            if count == mid:
                return curr
                break
            curr = curr.next
            count += 1
head = ListNode(10)
head.next = ListNode(20)
head.next.next = ListNode(30)
head.next.next.next = ListNode(40)
head.next.next.next.next = ListNode(50)
head.next.next.next.next.next = ListNode(60)


# Function call
result = Solution().middleNode(head)

# Print result
print("Node with value", result.val)

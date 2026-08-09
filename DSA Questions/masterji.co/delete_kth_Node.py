"""
Given a singly linked list, remove every **kth** node from the list (using 1 - based indexing). It is guaranteed that **k** is less than or equal to the length of the list. After removal, the remaining nodes should stay in their original order.

Input:  List: 1 → 2 → 3 → 4 → 5 → 6,  k = 2
Output: 1 → 3 → 5
Explanation: Every 2nd node (2, 4, 6) is removed, leaving 1, 3, and 5.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeEveryKthNode(self, head: ListNode | None, k: int) -> ListNode | None:
        if head is None:
            return None
            
        curr = head
        prev = None
        count = 1

        while curr:
            if count % k == 0:
                
                if prev is None:
                    head = curr.next
                    curr = head
                else:
                    prev.next = curr.next
                    curr = curr.next

            else:
                prev = curr
                curr = curr.next

            count += 1
        return head

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)

k = 2

sol = Solution()
head = sol.removeEveryKthNode(head, k)
curr = head

while curr:
    print(curr.val, end="")
    if curr.next:
        print(" -> ", end="")
    curr = curr.next
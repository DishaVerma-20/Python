# reverse a doubly linked list using the swap vala approach
class ListNode:
    def __init__(self, value=0, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class Solution:
    def swap_reverse(self, head):
        temp = head
        curr = head
        new_head = None
        while temp:
            curr = temp.next
            temp.next, temp.prev = temp.prev, temp.next

            new_head = temp
            temp = curr
        return new_head


head = ListNode(4)

node2 = ListNode(2)
head.next = node2
node2.prev = head

node3 = ListNode(3)
node2.next = node3
node3.prev = node2

node4 = ListNode(1)
node3.next = node4
node4.prev = node3

result = Solution().swap_reverse(head)

head = result
temp = head

while temp:
    if temp.next == None:
        print(temp.value, end = '')
    else:
        print(temp.value, end = " <-> ")
    temp = temp.next
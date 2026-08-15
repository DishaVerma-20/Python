# Reverse a doubly linked dlist using another approach
# ✅ Reverse order print karna hai → tumhara code sahi hai.
# ❌ DLL ko permanently reverse karna hai → tumhara code sufficient nahi hai; next/prev pointers change karne padenge.

class ListNode:
    def __init__(self, value=0, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class Solution:
    def reverse_dll(self, head):
        temp = head
        while head.next != None:
            head = head.next
        return head

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

result = Solution().reverse_dll(head)

head = result
curr = head
while curr.prev != None:
        print(curr.value, end = " <-> ")
        curr = curr.prev
if curr.prev == None:
    print(curr.value, end = '')

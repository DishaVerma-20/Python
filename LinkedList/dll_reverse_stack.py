# Reverse a doubly linked list using stack
class ListNode:
    def __init__(self, value=0, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class Solution:
    def reverse_stack(self, head):
        temp = head
        st = []

        while temp:
            st.append(temp.value)
            temp = temp.next

        temp = head

        while temp:
            temp.value = st.pop()
            temp = temp.next

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

result = Solution().reverse_stack(head)

temp = head
while temp:
    if temp.next == None:
        print(temp.value, end = '')
    else:
        print(temp.value, end = " <-> ")
    temp = temp.next
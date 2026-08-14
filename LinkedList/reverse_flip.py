class ListNode:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

class Solution:
    def reverse_linked_list(self, head):
        temp = head
        prev = None

        while temp != None:
            t1 = temp.next
            temp.next = prev
            prev = temp
            temp = t1
        return prev # reverse linked list ka head ho jayga

head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(2)
head.next.next.next = ListNode(5)

result = Solution().reverse_linked_list(head)

temp = result
while temp != None:
    if temp.next == None:
        print(temp.value, end = "")
    else:
        print(temp.value, end=" -> ")
    temp = temp.next
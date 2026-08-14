class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def stack_linkedList_palindromCheck(self, head):
        curr = head
        st = []
        while curr:
            st.append(curr.value)
            curr = curr.next

        curr = head
        # while curr:
        #     if curr.value == st.pop():
        #         curr = curr.next
        #     else:
        #         return False
        # return True

        while curr:
            if curr.value != st.pop():
                return False
            curr = curr.next

        return True

head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(1)

result = Solution().stack_linkedList_palindromCheck(head)
print(result)
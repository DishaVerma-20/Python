class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def palindrome_check_anotherApproach(self, head):
        curr = head
        temp = head
        prev = None

        while curr!=None:
            if curr.next == None:
                break 
            curr = curr.next

        while temp != curr:
            if curr.value != temp.value:
                      return False
            temp = temp.next
            # curr ke previous node ko find karo
            prev = head
            while prev.next != curr:
                prev = prev.next
            curr = prev
        return True

head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(1)

result = Solution().palindrome_check_anotherApproach(head)
print(result)

# space efficient hai, only pointers O(1)
# time efficient nhi hai, cause, bahar vala loop n/2 times approx, andar vala loop n times, then O(n^2)
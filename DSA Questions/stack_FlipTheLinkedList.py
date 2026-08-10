# Important Points:
# 1. Python list is used as a stack.
# 2. append() is used to push data into the stack.
# 3. pop() removes data from the top of the stack (LIFO).
# 4. The linked list nodes/links are not changed; only their data is changed.
# 5. Two traversals of the linked list are performed.

# Conclusion:
# The linked list is reversed using a stack by storing the data
# and then assigning it back in reverse order.

# Time Complexity: O(n)
# Space Complexity: O(n)
class Node:
    def __init__(self, data, next= None):
        self.data = data
        self.next = next

def reverse_using_stack(head):
    # creation of an empty stack
    stack = [] # using list

    curr = head

    while curr:
        stack.append(curr.data)
        curr = curr.next

    if not stack:
        return None

    curr = head
    while curr:
        curr.data = stack.pop()
        curr = curr.next

    return head

# creation of nodes
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

# print a linked list
def print_list(head):
    curr = head

    while curr:
        if curr.next == None:
            print(curr.data, end=' ')
        else:
            print(curr.data, end='->')

        curr = curr.next

print("Original Linked List:- ", end = '')
print_list(head)

reverse_using_stack(head)

print("\nReverse Linked List:- ", end = '')
print_list(head)
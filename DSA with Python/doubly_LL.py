# Doubly Linked List

class Node:
    def __init__(self, value=None):
        self.data = value
        self.next = None
        self.prev = None

class DoublyLL:
    # jitni linked list utne head, mtlb jitne object utne head
    def __init__(self):
        self.head = None
    
    def insertAtEnd(self, value):
        temp = Node(value)
        if (self.head == None):
            self.head = temp
            return
        
        t = self.head 
        while (t.next != None):
            t = t.next
        t.next = temp
        temp.prev = t

    def insertAtBeg(self, value):
        temp = Node(value)
        if self.head == None:
            self.head = temp
            return
        temp.next = self.head
        self.head.prev = temp   # doubly linked list
        self.head = temp

    def insertInMiddle(self, value, x):
        temp = Node(value)
        t = self.head
        while (t.next != None):
            if (t.data == x):
                temp.next = t.next
                t.next.prev = temp
                t.next = temp
                temp.prev = t
                break
            else:
                t = t.next

    def deletionDLL(self, value):
        t = self.head
        if (self.head == None):
            print("Linked List is empty")
            return
        elif (t.data == value):
            self.head = t.next
            t.next.prev = None
            return
        while (t.next != None):
            if (t.data == value):
                t.prev.next = t.next
                t.next.prev = t.prev.next
                return
            else:
                t = t.next
        if (t.data == value):
            t.prev.next = None
        
    def printDLL(self):
        t = self.head
        while (t.next != None):
            print(t.data, end = ' <--> ')
            t = t.next
        print(t.data)
    
obj = DoublyLL()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(40)
obj.insertAtBeg(1)
obj.insertInMiddle(50, 20)
obj.deletionDLL(1)
obj.deletionDLL(50)
obj.deletionDLL(40)
obj.printDLL()
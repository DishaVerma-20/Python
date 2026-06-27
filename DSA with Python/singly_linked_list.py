class node:
    def __init__(self, info, next = None):
        self.info = info
        self.next = next

class SinglyLL:
    def __init__(self, head = None):
        self.head = head

    def insertAtEnd(self, value):
        temp = node(value)
        # linked list is already there
        if (self.head != None): # linked list exists
            t1 = self.head
            while (t1.next != None):
                t1 = t1.next
            t1.next = temp
        
        # if linked list doesn't exists
        else:
            self.head = temp

    def insertAtBeg(self, value):
        temp = node(value)
        temp.next = self.head
        self.head = temp
    
    def insertInMiddle(self, value, x):
        temp = node(value)
        t1 = self.head
        # while (t1.info != x):
        #     t1 = t1.next
        while (t1.next != None):
            # t1 = t1.next
            if (t1.info == x):
                temp.next = t1.next
                t1.next = temp
                break
            else:
                t1 = t1.next

    def deleteLL(self, value):
        t1 = self.head
        prev = t1 
        if (t1.info == value):
            self.head = t1.next
        while (t1.next != None):
            if (t1.info == value):
                prev.next = t1.next
                break
            else:
                prev = t1 # pehle vale t1 ko point krega
                t1 = t1.next
        if (t1.info == value):
            prev.next = None


    def printLL(self):
        t1 = self.head
        while(t1.next != None):
            print(t1.info)
            t1 = t1.next
        print(t1.info)

obj = SinglyLL()
obj.insertAtEnd(34)
obj.insertAtEnd(40)
obj.insertAtBeg(1)
obj.insertInMiddle(20, 34)
obj.deleteLL(34)
obj.deleteLL(20)
obj.deleteLL(40)
obj.printLL()


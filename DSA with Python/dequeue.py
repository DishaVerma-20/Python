class Dequeue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items)==0
    
    def insertAtEnd(self, value):
        self.items.append(value)

    def insertAtStart(self, value):
        self.items.insert(0, value)

    def deletionFromBeg(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            return self.items.pop(0)

    def deletionFromEnd(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            return self.items.pop()

dq = Dequeue()
dq.insertAtEnd(10)
dq.insertAtStart(20)
dq.insertAtEnd(30)
dq.insertAtEnd(40)
dq.insertAtStart(50)
print(dq.deletionFromEnd())
print(dq.deletionFromEnd())
print(dq.deletionFromBeg())
print(dq.deletionFromBeg())
print(dq.deletionFromEnd())
dq.deletionFromEnd()
dq.deletionFromBeg()

    
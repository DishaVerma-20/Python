class Queue:
    def __init__(self):
        self.items = [] # hmne 1 list bna li

    # Underflow condition toh check krni pdegii
    def isEmpty(self):
        return len(self.items)==0
    
    # insertion hmesha hum rear mai krvayge, puchege nhi kha krana haiii
    def insert(self, value):
        self.items.append(value) # no need to check overflow vgera

    def delete(self):
        # if len(self.items)==0:
        if self.isEmpty():
            # raise Exception("Queue is empty")
            print("Queue is empty")
            return # agar ab yeh vala part true hai toh niche vala nahi chlega
        return self.items.pop(0)
    
q = Queue()
q.insert(10)
q.insert(20)
q.insert(30)

print(q.delete())
print(q.delete())
print(q.delete())
q.delete() # kyuki already print statement written in funxn
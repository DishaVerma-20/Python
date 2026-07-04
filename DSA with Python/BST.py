class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

def insert(root, value):
        if root == None:
            return Node(value)
        if root.data == value:
            return root
        if root.data>value:
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value)
        return root

def search(root, value):
        if root == None:
            print("Element not found", end = '\n')
            return
        if root.data == value:
            print("Element found", end = '\n')
            return
        if root.data>value:
            search(root.left, value)
        else:
            search(root.right, value)

def deletion(root, value):
    if (root == None):
        return root
    if (root.data>value):
        root.left = deletion(root.left, value)
    elif (root.data<value):
        root.right = deletion (root.right, value)
    else:
        if(root.left == None):
            return root.right
        if(root.right == None):
            return root.left
        else:
            succ = get_successor(root)
            root.data = succ.data
            root.right = deletion(root.right, succ.data)
    return root
        
def get_successor(root):
    root = root.right
    while (root != None and root.left != None): # agar root none hai toh vhi stop ho jaygaa
        root = root.left
    return root

    
def inorder(root):
    if root!=None:
        inorder(root.left)
        print(root.data, end = " ")
        inorder(root.right)

# root = Node(20)
# root.left = Node(15)
# root.right = Node(30)
# root.left.left = Node(12)
# root.left.right = Node(18)
# root.right.right = Node(40)
# inorder(root)

root = insert(None, 20)
root = insert(root, 15)
root = insert(root, 30)
root = insert(root, 40)
root = insert(root, 12)
root = insert(root, 18)
root = insert(root, 25)
root = insert(root, 50)

inorder(root)
print()
search(root, 18)
search(root, 100)

deletion(root, 12)
print('\n')
deletion(root, 20)
deletion(root, 40)
inorder(root)
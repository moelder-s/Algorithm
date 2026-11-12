class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

#Function to insert a value into the BST
def insert (root, value):
    if root is None:
        return Node (value)
    if value < root.data:
        root.left = insert(root.left,value)
    else:
        root.right = insert(root.right, value)
    return root

#Given numbers
numbers = [50,30,70,20,40,60,80]

#Start with an empty tree
root = None

#Insert all numbers into the BST
for num in numbers:
    root = insert(root,num)

#Display the root and its children
print("Root: ",root.data)#50
print("Left Child:",root.left.data) #30
print("Right Child: ", root.right.data) #70
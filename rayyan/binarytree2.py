class Node:
    def __init__(self,data):
        self.right = None
        self.left=None
        self.data= data
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data
def inorder(root):
    if root:
            inorder(root.left)
            print(str(root.data), end = ' ')
            inorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.data), end = ' ')
def preorder(root):
    if root:
        print(str(root.data), end= ' ')
        preorder(root.left)
        preorder(root.right)
root = Node(1)
root.insert(2)
root.insert(3)
root.insert(4)
root.insert(5)
print("inorder traversal")
inorder(root)
print("\npostorder traversal")
postorder(root)
print("\n preorder traversal")
preorder(root)
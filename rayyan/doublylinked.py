class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class ddl:
    def __init__(self):
     self.head=None
    def add(self,newdata):
        newnode=Node(newdata)
        newnode.next=self.head
        if self.head is not None:
            self.head.prev=newnode
        self.head=newnode
    def display(self,node):
        while(node is not None):
            print(node.data)
            last=node
            node = node.next
d=ddl()
d.add(12)
d.add(8)
d.add(62)
d.display(d.head)

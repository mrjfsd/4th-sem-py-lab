class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class slinkedlist:
    def __init__(self):
        self.head=None
    def display (self):
        d1 = self.head
        while d1 is not None:
            print(d1.data)
            d1=d1.next
l = slinkedlist()
l.head = Node("mon")
e1 = Node("tue")
e2 = Node("wed")
l.head.next=e1
e1.next =e2
l.display()



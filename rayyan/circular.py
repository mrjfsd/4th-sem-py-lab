class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class cll:
    def __init__(self):
        self.head=Node(None)
        self.tail=Node(None)
        self.head.next=self.tail
        self.tail.next=self.head
    def add(self,data):
        newNode=Node(data)
        if self.head.data is None:
            self.head=newNode
            self.tail=newNode
            newNode.next=self.head
        else:
            self.tail.next=newNode
            self.tail=newNode
            self.tail.next=self.head
    def display(self):
        current=self.head
        if self.head is None:
            print("list is empty")
            return
        else:
            print("node in list are")
            print(current.data)
            while(current.next !=self.head):
                current=current.next
                print(current.data)
a=cll()
a.add(1)
a.add(2)
a.add(3)
a.display()
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class slinkedlist:
    def __init__(self):
        self.head = None

    def display(self):
        d1 = self.head
        while d1 is not None:
            print(d1.data)
            d1 = d1.next

    def remove(self, remove):
        Head = self.head
        if (Head is not None):
            if Head.data == remove:
                self.head = Head.next
                Head = none
                return
        while (Head is not None):
            if (Head.data == remove):
                break
                prev = Head
                Head = Head.next
            if (Head == None):
                return
                prev.next = Head.next
                Head = None


l = slinkedlist()
l.head = Node("Monday")
e1 = Node("tuesday")
e2 = Node("wednesday")
l.head.next = e1
e1.next = e2
l.remove("tuesday")
l.display()

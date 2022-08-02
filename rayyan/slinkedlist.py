class Node:
    def _init_(self,data=None):
        self.data=data
        self.next=None
class slinkedlist:
    def _init_(self):
        self.head=None
    def display(self):
        d1=self.head
        while d1 is not None:
            print(d1.data)
            d1=d1.next
L=slinkedlist()
L.head =("tue")

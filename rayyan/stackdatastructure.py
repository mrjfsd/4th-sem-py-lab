class stack:
    def __init__(self):
      self.items=[]
    def isempty(self):
        return self.items==[]
    def push(self,data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
    def display(self):
        if self.items==[]:
            print("list is empty")
        else:
            for i in self.items:
                print(i)
s=stack()
while True:
    print("1.push <value>")
    print("2.pop")
    print("3.display")
    do=input("Enter the value for operation:").split()
    option=do[0].strip().lower()
    if option=="push":
        s.push(int(do[1]))
    elif option =="pop":
        if s.isempty():
            print("stack is empty")
        else:
            print("popped value : ", s.pop())
    elif option=='quit':
        break
    elif option == 'display':
        s.display()


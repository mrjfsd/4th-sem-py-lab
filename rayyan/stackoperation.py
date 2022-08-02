class stack:
    def __init__(self):
        self.items=[]
    def insempty(self):
        return self.items==[]
    def push(self,data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
    def display(self):
        for i in self.items:
            print(i)
s= stack()
while True :
    print('push <value>')
    print('pop')
    print('quit')
    do = input("Enter the value for operation : ").split()
    operation=do[0].strip().lower()
    if operation=="push":
       s.push(int(do[1]))
    elif operation =="pop":
        if s.insempty():
            print("stack is empty")
        else:
            print("popped value : ", s.pop())
    elif operation=='quit':
        break
    elif operation == 'display':
        s.display()

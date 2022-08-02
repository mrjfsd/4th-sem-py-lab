class postfix:
    def __init__(self,size):
        self.top=-1
        self.size=size
        self.array=[]
    def isempty(self):
        if (self.top==-1):
            return True
    def peek(self):
        return self.array[-1]
    def pop(self):
        if not self.isempty():
            self.top-=1
            return self.array.pop()
        else:
            return"$"
    def push(self,op):
        self.top+=1
        self.array.append(op)
    def Evaluate(self,exp):
        for i in exp:
            if i.isdigit():
                self.push(i)
            else:
                val1=self.pop()
                val2=self.pop()
                self.push(str(eval(val2+i+val1)))
        return int(self.pop())


exp="231*+9-"
obj=postfix(len(exp))
print("postfix expression %d"%obj.Evaluate(exp))

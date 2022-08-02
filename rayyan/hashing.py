class emp:
    def __init__(self,ename,eid):
        self.ename=ename
        self.eid=eid
    def __eq__(self,other):
        return self.ename==other.ename and self.eid==other.eid
    def __hash__(self):
        return hash((self.ename,self.eid))
E=emp("john",111)
print("THe hash is %d  "%hash(emp))
emp_copy=emp("john",111)
print("The hash is %d " %hash(emp_copy))
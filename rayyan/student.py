class Student:
    def __init__(self):
        self.data = []
    def insertstudent(self,sname,regid,result):
      self.data.append([sname,regid,result])
    def delstudent(self,regid):
         for row in self.data:
                    for i in row:
                        if i== regid:
                         self.data.remove(row)
    def searchstudent(self,regid):
        for row in self.data:
            for i in row:
             if i==regid:
                print(row)
    def displaystudent(self):
        for i in self.data:
            print(i)
e=Student()
e.insertstudent("rayyan",50,80)
e.insertstudent("kaleem",60,70)
e.displaystudent()
e.delstudent(2)
e.displaystudent()
e.searchstudent(1)


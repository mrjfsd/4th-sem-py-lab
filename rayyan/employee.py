class Employee:
    def __init__(self):
        self.data = []
    def insertemployee(self,sname,empid,salary):
      self.data.append([sname,empid,salary])
    def delemployee(self,empid):
         for row in self.data:
                    for i in row:
                        if i== empid:
                         self.data.remove(row)
    def searchemployee(self,empid):
        for row in self.data:
            for i in row:
             if i==empid:
                print(row)
    def displayemployee(self):
        for i in self.data:
            print(i)
e=Employee()
e.insertemployee("rayyan",201,8000)
e.insertemployee("kaleem",202,7500)
e.displayemployee()
e.delemployee(201)
e.displayemployee()
e.searchemployee(1)


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname,sid):
      super().__init__(fname,lname)
      self.sid = sid

  def getSid(self):
      return self.sid


class Teacher(Person):
    def __init__(self, fname, lname, tid, studentList=None):
        super().__init__(fname, lname)
        self.tid =tid
        if studentList == None:
            self.studentList = []
        else:
            self.studentList =[]
            for stu in studentList:
                self.studentList.append(stu)

    def show(self):
        print(self.firstname + " " + self.lastname)
        print(self.tid)
        print("-->" , self.studentList)
       

x = Student("Mike", "Olsen", 1258)
x.printname()
print(x.getSid())
teacher1 = Teacher("N", "P", 12345, [])
teacher1.show()
teacher2 = Teacher("A", "Meh", 12345, ["Nah", "Z"])
teacher2.show()


class Person:
    def __init__(self, status, fname, lname,Id):
        self.status=status
        self.firstname = fname
        self.lastname = lname
        self.Id=Id
    
    def display(self):
        print("Person Details:")
        print("  Status= {}".format(self.status))
        print("  Name= {} {}".format(self.firstname, self.lastname))
        print("  ID= {}".format(self.Id))


class Student(Person):
    def __init__(self, status, fname, lname,Id, graduationYear):
        super().__init__(status, fname,lname,Id)
        self.graduationYear = graduationYear

    def display(self):
        super().display()
        print("  Graduation Year is: {}".format(self.graduationYear))
        print("==================")


class Teacher(Person):
    def __init__(self, status, fname, lname, Id, course, studentList=None):
        super().__init__(status, fname, lname,Id)
        self.course =course
        if studentList == None:
            self.studentList = []
        else:
            self.studentList =[]
            for stu in studentList:
                self.studentList.append(stu)

    def addStudent(self,stu):
        self.studentList.append(stu)

    def removeStudent(self,stu):
        if len(self.studentList) == 0:
            print("The student {} does not exist.".format(stu))
        else:
            self.studentList.remove(stu)

    def display(self):
        super().display()
        print("  Course= {}".format(self.course))
        print("  Student List ------>" , self.studentList)
        print("==================")

student1 = Student("Student", "Mike", "Olsen", 125, 1999)
student1.display()
teacher1 = Teacher("Teacher", "John", "Li", 321, "Math", [])
teacher1.addStudent("Julia")
teacher1.display()
teacher2 = Teacher("Teacher", "Sarah", "Hamilton", 621,"History", ["Jojo", "Coco"])
teacher2.removeStudent("Coco")
teacher2.display()
teacher3= Teacher("Teacher", "David", "Gilbo", 876, "Science", [])
teacher3.display()
teacher3.removeStudent("Ray")

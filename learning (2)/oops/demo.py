class Student:

    rollno:int
    name:str
    course:str
    age:int

    def __init__(self,roln,nme,crse,age):
    # def add_student(self,roln,nme,crse,age):       
        self.rollno=roln
        self.name=nme
        self.course=crse
        self.age=age

    def get_student(self):
         print(self.rollno,self.name,self.course,self.age)

# obj1=Student()
# obj2=Student()

# obj1.add_student(56,"madavi","django",27)
# obj2.add_student(233,"akash","django",30)

# obj1.get_student()
# obj2.get_student()

obj1=Student(56,"narayani","msc maths",26)   # using constructor
obj2=Student(46,"anupama","msw",30)

obj1.get_student()
obj2.get_student()



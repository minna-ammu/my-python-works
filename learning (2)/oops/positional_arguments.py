class Student():           # ivide venel() ullil object nnn venel kodukkam. because ellathinteyum parent inheritance varunnath object il ninn ann
    rollno:int
    name:str
    course:str
    year:int

    def __init__(self,**kwargs):
        self.rollno=kwargs.get("rollno")
        self.name=kwargs.get("name")
        self.course=kwargs.get("course")
        self.age=kwargs.get("age")
    def get_student(self):
        print(self.rollno,self.name,self.course,self.age)
    # def __str__(self):       # oru object nte string method ne. obj ne print cheyyumpobol  basic ayitt name print akan and it is always string value (*)
    #     return self.name


obj=Student(rollno=134,name="kanjana",course="msw",age=27)
# obj.get_student()
print(obj)                   #  enthann object enn paryumbol basic ayitt parayuka name (*)

class School:
    classroom:int
    subjects:str
    books:int
    subject_instruments:int


    def classroom(self):
        print(4)
    def subjects(self):
        print("maths","physics","english","chemistry")
    def books(self):
        print(59)
    def subject_instruments(self):
        print(60)

class Tution_center(School):    # ivide school koduthath eth class il ninn inherit cheyyunnath nn 
    pass

obj=Tution_center()
obj.classroom()
obj.subjects()
obj.books()
obj.subject_instruments()

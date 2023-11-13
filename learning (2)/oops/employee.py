class Employee:
    
    id:int
    name:str
    designation:str
    salary:int

    def set_emp(self,idn,nme,dsgn,slry):
        self.id=idn
        self.name=nme
        self.designation=dsgn
        self.salary=slry

    def get_emp(self):
        print(self.id,self.name,self.designation,self.salary)

emp1=Employee()

emp1.set_emp(56,"adithya","hr",45000)
# emp1.get_emp()

# print(dir(Employee))
# print(dir(emp1))
print(emp1.__class__)
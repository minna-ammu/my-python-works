from abc import ABC,abstractmethod

class Employee(ABC):
    name=str
    salary=int

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    @abstractmethod
    def calculate_salary(self):
        pass

class Manager(Employee):
    
    def calculate_salary(self):
        return self.salary+20000
    
class Developer(Employee):
    def calculate_salary(self):
         return self.salary+40000
    
emp=Developer("madav",780000)
print(emp.calculate_salary())


    


    





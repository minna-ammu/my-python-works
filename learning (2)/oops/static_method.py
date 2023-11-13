import datetime     # datetime oru module an

class Operations:
    num1:int
    num2:int

    def __init__(self,n1,n2):
        self.num1=n1
        self.num2=n2

    def add(self):
        return self.num1+self.num2
    
    def product(self):
        return self.num1*self.num2
    @staticmethod
    def get_date():      # ivide self venda. because static method e class le attributes ne onnum accesss cheyyano modufy cheyyano padilla.
        return datetime.date.today()     # today oru method an7
    

number=Operations(45,56)
print(number.add())
print(number.product())     # mukalil return cheythath kond an ivide print kodukkunnath
print(Operations.get_date())
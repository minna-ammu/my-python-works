class Bank:

    acno:int
    balance:int
    ac_type:str
    p_name:str

    def create_account(self,acn,blnc,ac_typ,p_nme):
        self.acno=acn
        self.balance=blnc
        self.ac_type=ac_typ
        self.p_name=p_nme
        # print(self.acno,self.balance,self.ac_type,self.p_name)

    def deposit(self,amnt):
        self.balance+=amnt     # balance lott amount add cheyyunnu
        print(f" your sbi account {self.acno} has been credited with {amnt} aval balance is {self.balance}")


    def withdraw(self,amnt):
        if self.balance>=amnt:
            self.balance-=amnt
            print(f" your sbi account {self.acno} has been debited with the amount {amnt} aval balance is {self.balance}")
        else:
            print(f" transaction failed due to insufficient balance ")

obj1=Bank()
obj1.create_account(267,6000008,"saving account","Nikhitha")
obj1.deposit(20098.678)
# obj1.withdraw(2000)










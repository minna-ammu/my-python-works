class Mobiles:
    name:str
    price:int
    display:str

    def __init__(self,**kwargs):
        self.name=kwargs.get("name")
        self.price=kwargs.get("price")
        self.display=kwargs.get("display")

    def __str__(self):    # ith overriding ann. because already oru parent und object  class und
        return self.name
    
    def get_price(self):
        return self.price
    @property               # decorator used for converting methods into propert/attributes. then when get_discount calling no need of ().because it became property and in this funcion @property ; property is decorators name  
    def get_discount(self):
        return self.price-750
    

    
    
obj=Mobiles(name="oneplus",price=45000,display="amoled")
print(obj)
print(obj.get_price())
print(obj.get_discount)
    

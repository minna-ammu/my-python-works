class Books:
    name:str
    author:str
    pages:int
    price:int

    def __init__(self,**kwargs):
        self.name=kwargs.get("name")
        self.author=kwargs.get("author")
        self.pages=kwargs.get("pages")
        self.price=kwargs.get("price")

    def __str__(self):                  # obj nte string representation; nammal ara nn chothichal nammude pere matram adhym parayunna pole   (1)
          return self.name

obj=Books(name="randamoozham",author="mt",pages=560,price=670)
print(obj)               #(1)
        
    
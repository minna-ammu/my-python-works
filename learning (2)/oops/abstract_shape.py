from abc import ABC,abstractmethod

class  Shape(ABC):       # abstractclass ABC il ninn inherit cheyyunnu
    
    @abstractmethod       # decorator
    def draw (self):       # abstractmethod
        pass

class Rectangle(Shape):     # inherited from shape   
    
    def draw (self):               # shape  class  il ninn inherit cheyyunnu. so same nmethod as  shape ; draw
        print("drawing rectangle")

class Triangle(Shape):

    def draw(self):
        print("triangle drawing")

rctngle=Rectangle()
rctngle.draw()
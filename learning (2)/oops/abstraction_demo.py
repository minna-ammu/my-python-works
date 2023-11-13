from abc import ABC,abstractmethod

class Ide(ABC):

    @abstractmethod
    def debug (self):
        pass

class Pycharm(Ide):

    def debug (self):            #   inherited  from ABC
        print("pycharm debug method")

class Eclipse(Ide):

    def debug (self):               #   inherited  from ABC
        print("eclipse debug method") 

# pyc=Pycharm()
# pyc.debug()

elce=Eclipse()
elce.debug()


       
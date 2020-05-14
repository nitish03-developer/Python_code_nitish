from abc import ABC,abstractmethod

class DefenceForce(ABC):
    @abstractmethod
    def area(self):
        pass
    def gun(self):
        print('Gun = Ak47')

class Army(DefenceForce):
    def area(self):
        print("Area = Land")

class AirForce(DefenceForce):
    def area(self):
        print("Area = Sky")
       
class Navy(DefenceForce):
    def area(self):
        print("Area = Sea")
       
a=Army()
af=AirForce()
n=Navy()

a.gun()
a.area()
print()

af.gun()
af.area()
print()

n.gun()
n.area()
print()
       


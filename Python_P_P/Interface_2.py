from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def disp1(self):
        pass
    @abstractmethod
    def disp2(self):
        pass
        
class Child(Father):
    def disp1(self):
        print("Child Class")
        print("Disp 1 Abstarct Method")
        
class Grandchild(Child):
    def disp2(self):
        print("Grandchild class")
        print("Disp2 Abstract Method")
        
gc=Grandchild()
gc.disp1()
gc.disp2()
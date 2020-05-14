class Father:
    def __init__(self):
        print("Father class Constructor")
    def showF(self):
        print("Father class Method")

class Son(Father):
    def __init__(self):
        super().__init__()       #calling Father class Constructor
        print("Son class Constructor")
    def showS(self):
        print("Son class Method")

class Daughter(Father):
    def __init__(self):
        super().__init__()       #calling Father class Constructor
        print("Daughter class Constructor")
    def showD(self):
        print("Daughter class Method")

g=Daughter()
h=Son()

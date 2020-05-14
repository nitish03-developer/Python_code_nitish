class Father:
    def __init__(self):
        print("Father class Constructor")
    def showF(self):
        print("Father class Method")

class Son(Father):
    def __init__(self):
        super().__init__()   #Calling Father class Constructor
        print("Son class Constructor")
    def showS(self):
        print("Son Class Method")

class GrandSon(Son):
    def __init__(self):
        super().__init__()  #calling son class Constructor
        print("GrandSon class Constructor")
    def showG(self):
        print("GrandSon Class Method")

g=GrandSon()

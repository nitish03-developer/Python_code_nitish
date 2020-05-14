class Father:
    def showF(self):
        print("Father class Method")

class Son(Father):
    def showS(self):
        print("Son Class Method")

class GrandSon(Son):
    def showG(self):
        print("GrandSon Class Method")

g=GrandSon()
g.showG()
g.showF()
g.showS()

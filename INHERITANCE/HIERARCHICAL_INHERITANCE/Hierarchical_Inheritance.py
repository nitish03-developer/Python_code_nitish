class Father:
    def showF(self):
        print("Father class Method")

class Son(Father):
    def showS(self):
        print("Son class Method")

class Daughter(Father):
    def showD(self):
        print("Daughter class Method")

r=Daughter()
r.showF()
r.showD()
print()

f=Son()
f.showF()
f.showS()

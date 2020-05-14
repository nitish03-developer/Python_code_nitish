class Father:
    def showF(self):
        print("Father class Method")

class Mother:
    def showM(self):
        print("Mother class Method")

class Son(Father,Mother):
    def showS(self):
        print("Son class Method")

h=Son()
h.showF()
h.showM()
h.showS()

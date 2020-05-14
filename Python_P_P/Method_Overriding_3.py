class Add:
    def result(self,x,y):
        print("Addition:",x+y)

class Multi(Add):
    def result(self,a,b):
        super().result(50,20)
        print("Multiplication: ",a*b)

m=Multi()
m.result(10,20)


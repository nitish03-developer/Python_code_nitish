class Father:       #Parent class
    def __init__(self):   #Constructor
        self.money=1000   # instance variable   
        print("Father Class constructor")    

    def show(self):        #instance method
        print("Father class Instance Method")

class Son(Father):        #Child class
    def __init__(self):   #Constructor
        super().__init__() #calling parent class constructor
        print("Son Class Consructor",self.money)

    def disp(self):       #instance method
        print("Son class Instance Method",self.money)

s=Son()         #create object Son class
s.disp()


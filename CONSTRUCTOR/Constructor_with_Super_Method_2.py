class Father:       #Parent class
    def __init__(self,m):   #Constructor
        self.money=m   # instance variable   
        print("Father Class constructor")    

    def show(self):        #instance method
        print("Father class Instance Method")

class Son(Father):        #Child class
    def __init__(self,m,j):   #Constructor
        super().__init__(m) #calling parent class constructor
        self.job=j
        print("Son Class Consructor",self.money)

    def disp(self):       #instance method
        print("Son class Instance Method",self.money)
        print("Job", self.job)

s=Son(1000,'Python')         #create object Son class
s.disp()


class Father:       #Parent class
    def __init__(self):   #Constructor
        self.money=1000   # instance variable   
        print("Father Class constructor")    

    def show(self):        #instance method
        print("Father class Instance Method")

class Son(Father):        #Child class
    def __init__(self):   #Constructor
        self.money=5000   #instance variable
        self.car="BMW"    # instance variable
        print("Son Class Consructor")

    def disp(self):       #instance method
        print("Son class Instance Method")

s=Son()         #create object Son class
print(s.money)  #calling instance variable of the son class
print(s.car)    #calling instance variable of the son class
s.disp()        #calling disp method
print()

f=Father()      #create object Father class
print(f.money)  # calling instance variable of the Father class through Father class object
        

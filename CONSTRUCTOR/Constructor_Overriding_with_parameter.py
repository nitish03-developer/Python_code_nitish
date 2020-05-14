class Father:       #Parent class
    def __init__(self,m):   #Constructor
        self.money=m   # instance variable   
        print("Father Class constructor")    

    def show(self):        #instance method
        print("Father class Instance Method")

class Son(Father):        #Child class
    def __init__(self,r):   #Constructor
        self.money=r   #instance variable
        self.car="BMW"    # instance variable
        print("Son Class Consructor")

    def disp(self):       #instance method
        print("Son class Instance Method")

s=Son(2000)         #create object Son class
print(s.money)  #calling instance variable of the son class
print(s.car)    #calling instance variable of the son class
s.disp()        #calling disp method
s.show()        #calling show method through child class object by the process of inheritance
print()

f=Father(1000)      #create object Father class
print(f.money)  # calling instance variable of the Father class through Father class object
        

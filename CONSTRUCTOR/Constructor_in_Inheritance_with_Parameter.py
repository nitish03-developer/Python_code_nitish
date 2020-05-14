class Father:   #parent class
    def __init__(self,m):   
        self.money=m   #instance variable
        print("Father class Constructor")
    def show(self):     #instance method
        print("Father class Instance Method")

class Son(Father): #child class
    def disp(self):  #instance method
        print("Son Class Instance Method",self.money) # Accessing constructor of Father class in Son class

s=Son(4000)       #object  created from son class
print(s.money) #calling instance method of parentclass through child class object
s.show()   #calling show method through son class object
s.disp()   # calling disp method

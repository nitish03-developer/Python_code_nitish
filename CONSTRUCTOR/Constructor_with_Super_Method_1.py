class Father:       #Parent class
    def __init__(self):   #Constructor   
        print("Father Class constructor")    

    def show(self):        #instance method
        print("Father class Instance Method")

class Son(Father):        #Child class
    def __init__(self):   #Constructor
        super().__init__()
        print("Son Class Consructor")

    def disp(self):       #instance method
        print("Son class Instance Method")

s=Son()         #create object Son class

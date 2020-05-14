class Mobile:
    def __init__(self,m):         # Constructor initialization
        self.model=m               # instance variable
        
    def show_model(self,p):       # instance method
        self.price=p            # local variable
        print("Model: ", self.model, "Price: ", self.price) #Accessing the instance and local variable
    
realme=Mobile('Realme X2')     # creating object1
realme.show_model(1000)        # Accessing instance method with actual argument
print(id(realme))              
print()



realme1=Mobile('Realme X2')    #creating object2
realme1.show_model(1000)       #Accessing instance method with actual argument
print(id(realme1))
print()

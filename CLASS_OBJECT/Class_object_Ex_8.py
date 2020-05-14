class Mobile:
    def __init__(self,m):     # Constructor with formal Arguments
        self.model=m          # instance variable
        
    def show_model(self,p):   # instance method with formal arguments
        self.price=p         # Local variable
        #print("Model: ", self.model, "Price: ", price)
        print("Model: ", self.model, "Price: ", self.price) # accessing local and instance variable        
        
realme = Mobile('RealMe X')   # creating object and passing actual Arguments to the constructor
realme.show_model(1000)      # call instance method and passing actual arguments to the method
print(id(realme))             # Address of the given Object
print()

redmi = Mobile('Redmi')   # creating object and passing actual Arguments to the constructor
redmi.show_model(2000)      # call instance method and passing actual arguments to the instance method
print(id(redmi))
print()

Nokia = Mobile('Nokia 6.0')   # creating object and passing actual Arguments to the constructor
Nokia.show_model(3000)      # call instance method and passing actual arguments to the method
print(id(Nokia))
print()

class Mobile:
    def __init__(self,m):     # Constructor with formal Arguments
        self.model=m          # instance variable
        
    def show_model(self,p):   # instance method with formal arguments
        self.price=p               # Local variable
        #print("Model: ", self.model, "Price: ", price)
        print("Model: ", self.model, "Price: ", self.price) #accesing local and instance variable        
        
realme = Mobile('Redmi')   # creating object and passing actual Arguments to the constructor
realme.show_model(1000)      # call instance method and passing actual arguments to the method
print(id(realme))
print()

redmi = Mobile('Redmi')   # creating object and passing actual Arguments to the constructor
redmi.show_model(1000)      # call instance method and passing actual arguments to the method
print(id(redmi))
print()

Nokia = Mobile('Redmi')   # creating object and passing actual Arguments to the constructor
Nokia.show_model(1000)      # call instance method and passing actual arguments to the method
print(id(Nokia))
print()

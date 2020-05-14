class Mobile:
    def __init__(self,m):     # Constructor with formal Arguments
        self.model=m          # instance variable
        
    def show_model(self,p):   # instance method with formal arguments
        price=p               # Local variable
        print("Model: ", self.model, "Price: ", price) # Accesing instance and local variable
        #print("Model: ", self.model, "Price: ", self.price)         
        
realme = Mobile('RealMe X')   # creating object and passing actual Arguments to the constructor
realme.show_model(1000)      # call instance method and passing actual arguments to the method

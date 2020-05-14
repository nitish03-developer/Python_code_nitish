class Mobile:
    def __init__(self):     # Constructor to initialize the instance variable
        self.model='RealMe X'   # instance variable
        
    def show_mode(self):    # instance method
        print("Model: ", self.model) # accessing the instance variable with in the class
    
realme=Mobile()          # creating object

print(realme.model) #Accessing instance variable using object outside of the class

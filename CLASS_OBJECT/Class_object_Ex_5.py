class Mobile:
    def __init__(self):         # Constructor to initialize the instance variable
        self.model ='RealMe X'  # instance variable
        
    def show_model(self):       # instance Method
        price=1000              # local variable
        print("Model: ", self.model, "Price: ", price) # Accessing instance variable
    
realme = Mobile()               # creating object
realme.model='Realme Pro2'      # assign new value to the instance vriable through object outside of the class
print(realme.model)             # Accessing instance variable using object
realme.show_model()             # Accessing instance method using object
            

class Mobile:
    def __init__(self):      # creating constructor for initializing the instance variable
        self.model='RealMe X'  # instance variable
        
    def show_model(self):      #  instance method
        print("Model:  ", self.model)   # accessing the instance variable within the class
        
        
realme=Mobile()           # creating object 
realme.show_model()       # calling instance method using object outside the class
        
            

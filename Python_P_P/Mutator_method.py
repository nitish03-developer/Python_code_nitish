# Instance Method - Mutator Method / setter Method

class Mobile:
    def __init__(self):       # Constructor
        self.model="Realme X" #instance variable

    def set_model(self):      #Mutator Method
        self.model="Realme 2" 

realme=Mobile()
print(realme.model)
realme.set_model()  # calling Mutator method
print(realme.model)

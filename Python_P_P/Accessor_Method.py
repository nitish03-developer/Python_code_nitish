# Instance Method - Accesor Method / Getter Method

class Mobile:
    def __init__(self):       # Constructor
        self.model="Realme X" #instance variable

    def get_model(self):      #Accessor Method
        return self.model

realme=Mobile()
m=realme.get_model()  # calling accesor method
print(m)

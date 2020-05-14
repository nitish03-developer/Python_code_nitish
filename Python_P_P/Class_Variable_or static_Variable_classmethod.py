class Mobile:
    fp="yes"    # class variable / static variable

    def __init__(self):
        self.model="RealMe X"      # instance variable
    def show_model(self):          # instance Method
        print("Model: ",self.model) # Accessing instance variable

    @classmethod                     # class method
    def car(cls):
        print("Finger Print: ", cls.fp) # Accessing class variable


realme=Mobile()   # object creation
realme.show_model()  # Accessing instance method outside the class
Mobile.car()    # Accessing class method outside the class
print()
Mobile.fp="No"   # Change the value of class variable/static variable using class
Mobile.car()     # Accessing class method outside the class

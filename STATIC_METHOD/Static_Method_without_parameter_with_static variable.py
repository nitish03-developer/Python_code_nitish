class Mobile:
    fb="yes"              #static variable

    @staticmethod     #Decorator
    def show_model():       #static method
        print("Realme X")
        print("Finger print: ",Mobile.fb) #Accessing static variable within the Staic method

realme=Mobile()
realme.show_model()    # calling static method

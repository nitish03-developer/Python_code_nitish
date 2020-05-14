class Mobile:
    fb="yes"         #class variable

    @classmethod      #Decorator
    def show_model(cls,r):  # class method with formal parameter
        cls.ram=r           #local variable
        print("Finger print: ",cls.fb)  # Accesing class variable within the method
        print("Ram: ",cls.ram)     #Accessing local variable within the method

realme=Mobile()   #object
Mobile.show_model('4GB')  #Accessing method class outside the class with class name with actual argument

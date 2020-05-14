class Mobile:
    fb="yes"     #class Variable

    @classmethod   #Decorator
    def show_model(cls):  #class method
        print("finger Print: ", cls.fb)

realme=Mobile()
Mobile.show_model()  #calling class method outside the class with class name
    

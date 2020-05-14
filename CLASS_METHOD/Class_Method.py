class Mobile:
    @classmethod   #Decorator
    def show_model(cls):  #class method
        print("Realme x")  

realme=Mobile()        #object
Mobile.show_model()    #calling class method with class method

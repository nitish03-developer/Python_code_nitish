class Mobile:

    @staticmethod    #decorator
    def show_model(m,p):    #static method with parameter
        model=m              #local variable
        price=p              #local variable
        print("Model: ", model) #Accessing local variable  within the static method
        print("price: ", price) #Accessing local variable  within the static method

realme=Mobile()
Mobile.show_model("Realmex",1000)

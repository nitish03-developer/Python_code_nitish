class Mobile:
    fb="yes"      #class variable /static variable

    @classmethod
    def moto(cls): # class method
        print("Finger Print: ",cls.moto)  #Accessing class variable

realme=Mobile()   # object1 create
redmi=Mobile()  # object2 create
geek=Mobile()   # object3 create

print("Realme: ", Mobile.fb)   # Accessing class variable with class name
print("Redmi: ", Mobile.fb)
print("Geek: ",Mobile.fb)

# class variable can create only one copy of each object
print()
Mobile.fb="No"          # Modifying class variable using class 
print("Realme: ", Mobile.fb)
print("Redmi: ", Mobile.fb)
print("Geek: ",Mobile.fb)


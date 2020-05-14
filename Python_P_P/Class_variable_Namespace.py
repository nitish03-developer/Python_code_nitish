class Mobile:
    fb="yes"      #class Variable

    @classmethod
    def moto(cls):    #class method
        print("FInger Print: ",cls.fb)   #Accessing class variable within the class method

realme=Mobile()  #object1
redmi=Mobile() # object2
geek=Mobile() # Object3

print("Class Fb: ", Mobile.fb) #Accesiing class variable ouside with class name
print("Realme: ", realme.fb)   #Accessing class variable outside the class with object
print("Redmie: ", redmi.fb)
print("Geek: ", geek.fb)

print()
realme.fb="Not Working"   # Modifiying class variable with object
print("Class Fb: ", Mobile.fb) #Accesiing class variable ouside with class name
print("Realme: ", realme.fb)   #Accessing class variable outside the class with object
print("Redmie: ", redmi.fb)
print("Geek: ", geek.fb)
print()

Mobile.fb="No"   # Modifying class variable with class name
print("Class Fb: ", Mobile.fb) #Accesiing class variable ouside with class name
print("Realme: ", realme.fb)   #Accessing class variable outside the class with object
print("Redmie: ", redmi.fb)
print("Geek: ", geek.fb)



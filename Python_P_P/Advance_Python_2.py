class Nitish:
    def __init__(self,m,n):   # Constructor with parameter
        self.gf=m             # instance variable
        self.ex_gf=n          # instance variable
    def girls(self,year,year1):  #instance Method with parameter
        self.duration=year       #local variable
        self.duration1=year1     #local Variable
        print("Present_GF: ", self.gf, "Duration: ", self.duration) #Accessing instance and local variable
        print("Ex_Gf: ", self.ex_gf, "Duration: ", self.duration1)  #Accesing instance and local variable
mahato=Nitish("Chinu","Anchal") # Creating object and passing actual argument
mahato.girls(2017,2019)    # Accessing instance method and passing actual argument

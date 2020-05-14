class Nitish:
    def __init__(self,m,n):         # Constructor with formal argumnet
        self.var_1=m                # instance variable
        self.var_2=n                # instance variable
    def values(self):               # instance Method
        print("Variable_1", self.var_1) # Accessing instance variable within class
        print("Variable_2", self.var_2) # Accessing instance variable within class
kumar=Nitish(4,5)                   # Object create
kumar.values()                      # Calling instance method through object
print()
print(kumar.var_1)                  # Accessing instance variable outside the class

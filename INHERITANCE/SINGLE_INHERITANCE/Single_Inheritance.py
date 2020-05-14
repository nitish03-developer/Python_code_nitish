class Father:        #Parent class
    money=1000         #class variable

    def show(self):   #instance method
        print("Parent class Instance Method")

    @classmethod
    def showmoney(cls):  #class Method
        print("Parent class Class method: ", cls.money)  #Accessing class variable in class method
    @staticmethod        #static method
    def stat():
        print("Parent class Static method: ", Father.money) #Accessing class variable in static method

class Son(Father):       #Child Class
    def disp(self):       #instance method
        print("Child class Instance Method")
s=Son()                #creating object for child class
print()
s.disp()             # calling disp function from child class
print()
s.show()             #calling show function from Parent class
print()
s.showmoney()        #calling showmoney from parent class
print()
s.stat()             #calling stat function from parent class
print()
print("*******************************")
f=Father()           #creating object for parent class
print()
f.show()            #calling show function from parent class
print()
f.stat()            #calling stat function from parent class
print()
f.showmoney()       #calling show_money function from parent class
print()

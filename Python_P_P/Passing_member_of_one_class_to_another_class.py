class Student:
    def __init__(self,m,r):    #Constructor
        self.name=m      #instance variable
        self.roll=r      #instance variable

    def disp(self):    #instance method
        print("Name: ", self.name)   #Accessing instance variable within the method
        print("Roll: ", self.roll)   #Accessinf instance variable within the method

class User:
    @staticmethod
    def show(s):
        print("User Name: ",s.name)
        print("User Roll: ",s.roll)
        s.disp()

stu=Student("Rahul",102)
User.show(stu)

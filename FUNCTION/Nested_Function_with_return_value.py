# Defining a function
def disp(st):
    def show():
        return("Show Function")
    result=show()+ st+ "Disp Function"
    return result
    
              # Calling inner function
a=disp("Nitish")     # calling outter function
print(a)

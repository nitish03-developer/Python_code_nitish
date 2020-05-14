def disp(sh):
    print("Disp Function"+sh())

def show():
    return "Show Function"
disp(show)

print("****************************************")
def disp(sh):
    return("Disp Function"+sh())

def show():
    return "Show Function"
a=disp(show)
print(a)

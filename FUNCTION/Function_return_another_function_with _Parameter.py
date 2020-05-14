def disp(sh):      # Formal Argument
    print("Disp Function")
    return sh

def show():
    return "Show function"
r=disp(show)    # Actual argument
print(r())

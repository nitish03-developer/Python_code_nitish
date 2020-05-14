def disp():
    def show():
        return "Show function"
    print("Disp Function")
    return show
r=disp()
print(r())

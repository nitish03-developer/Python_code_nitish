class Army:       #outer class
    def __init__(self):
        self.name="Rahul"
        self.gun=self.Gun()     #creating inner class Object

    def show(self):
        print("Name: ", self.name)

    class Gun:     #inner class
        def __init__(self):
            self.name="AK47"
            self.capacity="75 Rounds"
            self.length="34.3 In"
        def disp(self):
            print("Gun Name: ", self.name)
            print("Capacity: ", self.capacity)
            print("Length: ", self.length)
a=Army()
print(a.name)
a.show()
print(a.gun.name)
g=a.gun
print()
print(g.name)
print(g.capacity)
print(g.length)
print()
g.disp()

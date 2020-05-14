a={10,20,5,10,30}
print("Before clear:",a)
print(id(a))
a.clear()
print("After clear",a)
print(id(a))

for element in a:
    print(element)

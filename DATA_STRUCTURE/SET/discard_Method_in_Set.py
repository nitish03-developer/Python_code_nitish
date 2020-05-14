b={10,20,"Nitish","Mahato",40,10,}
print("Original Set", b)
print(id(b))
print()

b.discard("Kendua")
print("After Removing set",b)
print(id(b))
a=[10,20,30,40,50]
b=a.copy()
print("A : ",a)
print("ID of A: ", id(a))
print("B : ",b)
print("ID of B: ", id(b))

print()

b=a[0:5]
print("A : ",a)
print("ID of A: ", id(a))
print("B : ",b)
print("ID of B: ", id(b))
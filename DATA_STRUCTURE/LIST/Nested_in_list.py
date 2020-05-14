a=[10,20,30,[50,60]]
print("Before Modification A: ",a)

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[3][0])
print(a[3][1])


print()
a[1]=100
a[3][0]=5
print("After modification A: ",a)
print()

a=[10,20,30]
b=[50,60,a]
print(b)
print(a)

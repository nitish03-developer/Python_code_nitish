a=[]
n=int(input("Enter Number of element: "))
print(a)
for i in range(n):
    a.append(int(input("Enter Element: ")))

print(type(a))
a=tuple(a)

for element in a:
    print(element)

print(a)
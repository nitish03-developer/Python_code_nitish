a={"Nitish","Ankur","Rahul","Vishal"}
b={"Nitish","Prem","Neha"}

g=a.intersection(b)
print(g)

h=a.union(b)
print(h)

l=a.difference(b)
print(l)

k=a.issubset(b)
print(k)
print()

k=a.issuperset(b)
print(k)
a={"Nitish"}
b={"Nitish"}
k=a.issubset(b)
print(k)

a={"Nitish","Ankur","Rahul","Vishal"}
b={"Nitish"}
k=a.issuperset(b)
print(k)
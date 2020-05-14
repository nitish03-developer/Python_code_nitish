a=set()
a.update([101,102,103])
print(a)


b={10,20,"Nitish","Mahato",40,10,}
print(id(b))
x=[101,102,103]
b.update(x)
print(b)
print(id(b))
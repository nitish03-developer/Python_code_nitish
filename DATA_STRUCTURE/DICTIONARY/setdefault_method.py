stu={101:'Rahul',102:'Nitish',103:'Sonam'}

print("Original Dict")
print(stu)
print(id(stu))
print()

returned_value=stu.setdefault(109)

print("After Setdefault Dict")
print(stu)
print(id(stu))

print("Returned value:", returned_value)
print()
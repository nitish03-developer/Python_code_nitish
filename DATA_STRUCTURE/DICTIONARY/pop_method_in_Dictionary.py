stu={101:'Rahul',102:'Nitish',103:'Sonam'}

print("Original Dict")
print(stu)
print(id(stu))
print()

removed_value=stu.pop(102)

print("After removing Dict")
print(stu)
print(id(stu))

print("Removed Value:", removed_value)
print()
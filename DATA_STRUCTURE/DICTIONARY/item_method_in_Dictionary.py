stu={101:'Rahul',102:'Nitish',103:'Chinu'}

print("Original Dict: ")

print(stu)

print()

it=stu.items()
print(it)
print(type(it))
print()

lst=list(it)
print(lst)
print(type(lst))
print()

print(lst[0])
print(lst[1])
print(lst[2])
for r in lst:
    for c in r:
        print(c)
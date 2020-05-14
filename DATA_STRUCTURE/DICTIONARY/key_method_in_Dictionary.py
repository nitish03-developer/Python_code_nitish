stu={101:'Mukesh',102:'Nitish',103:'Chinu'}

print("Original Dict: ")
print(stu)
print()

all_keys=stu.keys()

print(all_keys)
print(type(all_keys))
print()

key_list=list(all_keys)
print(key_list)
print(type(key_list))

for i in key_list:
    print(i)
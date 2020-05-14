def show(l):
    print(l)
    print(type(l))
    for i in l:
        print(i)
    return l

lst=[10,20,30,'Geekyshows']
new_lst=show(lst)
print(new_lst)
print(type(new_lst))


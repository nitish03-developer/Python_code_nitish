# remove_method:- remove the particular element
from array import*
stu_roll=array('i',[101,102,100,104,105])
arr=array('i',[108,109])
n=len(stu_roll)
i=0
while i<n:
    print(stu_roll[i])
    i+=1

print("Array after Extend")

stu_roll.extend(arr)
n=len(stu_roll)
i=0
while i<n:
    print(stu_roll[i])
    i+=1


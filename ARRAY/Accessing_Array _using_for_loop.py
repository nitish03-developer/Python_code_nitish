#without index
from array import*
stu_roll=array('i',[101,102,103,104,105])
for element in stu_roll:
    print(element)

print("*********************************************************")

# with index
from array import*
stu_roll=array('i',[101,102,103,104,105])
n=len(stu_roll)
for element in range(n):
    print(element,"=",stu_roll[element])




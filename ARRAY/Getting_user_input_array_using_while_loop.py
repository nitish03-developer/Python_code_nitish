from array import*
stu_roll=array('i',[])
n=int(input("Enter the Number of Element"))
i=0
while i<n:
    stu_roll.append(int(input("Enter element")))
    i+=1

j=0
while j<(len(stu_roll)):
    print(stu_roll[j])
    j+=1

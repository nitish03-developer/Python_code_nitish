num=int(input("Enter the Number"))
temp=0
a=range(2,num,1)
for i in a:
    if(num%i==0):
        temp=temp+1
if(temp==0):
    print("It is Prime Number")
else:
    print("It is not Prime")

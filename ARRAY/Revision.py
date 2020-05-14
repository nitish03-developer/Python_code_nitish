from array import*
arr=array('i', [])
n=int(input("Enter the Number of Element"))
for i in range(n):
    arr.append(int(input("Enter the Element")))

n=len(arr)  
for i in arr:
    print(i)
    
print("*****************************************")

for i in range(n):
    print(i,"=",arr[i])
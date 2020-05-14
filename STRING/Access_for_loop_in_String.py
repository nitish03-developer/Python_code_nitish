str1="NitishMahato"
n=len(str1)

for i in range(n):
    print(i,"=",str1[i])
    
    
print("*********Without Index****************")
    
for i in str1:
    print(i)
    
print("**************While_loop***********")

i=0
while i<n:
    print(str1[i])
    i+=1
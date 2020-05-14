name=input("Enter the Consumer Name")
n=int(input("Enter the Consumer Number"))
u=int(input("Enter the Consumed Units"))
if(u<=100):
    print("Total_Pay Rs ",u*6.25)
else:
    if((u>100)and(u<=200)):
        print("Total_Pay Rs ",100*6.25+(u-100)*6.39)
    else:
        if((u>200)and(u<=300)):
            print("Total_Pay Rs ",100*6.25*+200*6.39+(u-200)*7.21)
        else:
            if(u>300):
                print("Total_Pay Rs ",100*6.25+200*6.39+300*7.21+(u-300)*7.56)
                
        


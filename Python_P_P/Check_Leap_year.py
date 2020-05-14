num=int(input("Enter the Year  "))
if(num%4==0):
    if(num%100==0):
        if(num%400==0):
            print(num,"It is Leap year")
        else:
            print(num,"is not a Leap Year")
    else:
        print(num,"is Leap Year")
else:
    print(num,"is not a leap Year")

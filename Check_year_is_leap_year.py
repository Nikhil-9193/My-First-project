Y=int(input("Enter Year :- "))
if Y%4==0:
    if Y%100==0:
        if Y%400==0:
            print("Year is Leap Year")
        else:
            print("Year is Not Leap Year")
    else:
        print("Year is leap Year")
else:
    print("Year is Not Leap Year")
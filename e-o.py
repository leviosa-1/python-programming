n=int(input("Enter the range to get even odd numbers"))
for i in range(1,n+1) :
    if i%2==0 :
        print("even :",i,end=" ")
    else :
        print("odd :",i,end=" ")

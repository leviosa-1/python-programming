n=int(input("Enter number to get its multiplicatioon table"))
# armstrong number 
s=n
b=len(str(n))
sum=0
while n!=0:
    r=n%10
    sum=sum+(r**b)
    n=n//10
if s==sum:
    print(f"{s} is armstrong number")
else :
    print(f"{s } is not arrmstrong number")
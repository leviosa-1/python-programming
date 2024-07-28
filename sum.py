def sum_sq(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i**2
    return sum
n=int(input("Enter natural number to get its sum "))
sum=0

for i in range(1,n+1):
    sum=sum+i
print(f"sum of given number {n} is {sum}")
print(f"sum of square of natural n upto {n} is : {sum_sq(n)}")                                                                                                                                                          
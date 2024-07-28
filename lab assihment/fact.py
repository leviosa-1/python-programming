def factorial(num):
    # factorial = n*(n-1)
    if num==0:
        return 1
    else:
        return num*factorial(num-1)
    

num=int(input("ENter number to find its factorial"))
fact=1

for i in range(1,num+1):
    fact=fact*i
    
print("factorial of ",num, " is ",fact)
result=factorial(num)
print(f"factorial of {num} is : {result}")
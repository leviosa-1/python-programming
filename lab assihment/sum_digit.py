def sum_of_digit(digit):
    num=str(digit)
    sum=0
    for i in num :
        sum=sum+int(i)
    return sum
digit=int(input("Enter a digit to get its sum of digit:"))
print(f"SUm of given digit {digit} is : {sum_of_digit(digit)}")
 
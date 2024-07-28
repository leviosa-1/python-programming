def dtb(decimal):
    binary=""
    while decimal>0:
        rem=decimal%2
        binary=str(rem)+binary
        decimal=decimal//2
    return binary

decimal=int(input("Enter a decimal digit"))
print(f"The binary form of given decimal {decimal} is {dtb(decimal)} ")

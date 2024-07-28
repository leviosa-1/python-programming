def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    gcd = find_gcd(a, b)
    lcm = (a * b) // gcd
    return lcm

# Input two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate and print the LCM
lcm = find_lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is {lcm}.")
 
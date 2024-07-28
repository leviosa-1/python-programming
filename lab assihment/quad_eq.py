# ax^2+bx+c=0 quadratic equation solution
import cmath # complex math module for handling complex numbers
def quadratic_solver(a,b,c):
    d= b**2-4*a*c
    if a==0:
        return -(c/b)
    root1= (-b + cmath.sqrt(d)) /2*a
    root2= (-b - cmath.sqrt(d))/2*a
    return root1 , root2

a=int(input("Enter the coefficient of x^2 :"))
b=int(input("Enter the coefficient of x :"))
c=int(input("Enter the coefficient :"))
solutions = quadratic_solver(a,b,c)
print("the Roots of quadratic equations are :",solutions)

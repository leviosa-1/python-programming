import math as m
class calculator:
    def __init__(sel,n):
        sel.n=n
    
    @staticmethod
    def greet():
        print("Hello")
        
    
    def sq(self):
         print(f"Square of {self.n} is : {self.n**2}")
    
    
    def cube(self):
        print(f"Cube of {self.n} is : {self.n**3}")
    
    def sqr(self):
       print(f"Square root of {self.n} is {m.sqrt(self.n)}")
    
n=int(input("Enter n:"))
c=calculator(n)
c.greet()
c.sq()
c.cube()
c.sqr()

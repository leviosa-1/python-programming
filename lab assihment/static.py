class Maths_Operations:
    @classmethod
    def add(self,x,y):
        print(f"Additon: {x+y}")
        
    @classmethod
    def sub(self,x,y):
        if x > y:
            print("Substration :", x-y)
        else:
            print("Substraction :",y-x)
            
    @staticmethod
    def multiply(x,y):
        print("multiply :",x*y)
    
        
m=Maths_Operations()
m.add(10,20)
m.sub(30,20)

Maths_Operations.multiply(5,10)
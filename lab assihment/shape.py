class Shape:
    def area(self):
        pass

class circle(Shape):
    def area(self,r):
        super().area()
        area=3.14*r**2
        print("Area of circle :",area)
        
class rectangle(Shape):
    def area(self,l,b):
        super().area()
        area=l*b
        print("Area od Rectangle:",area)
c = circle()
c.area(5)
r = rectangle()
r.area(5,10)

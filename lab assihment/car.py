class car:
    def __init__(self,color,model):
        self.color=color
        self.model=model
    
    def display_info(self):
        print("MOdel No : ",self.model)
        print("Color : ",self.color)

class ElectricCar(car):
    def __init__(self,color,model,Battery_size):
        super().__init__(color,model)
        self.Battery_size=Battery_size
    
    def display_info(self):
        super().display_info()
        print("Battery Size :",self.Battery_size ,"kWh")

color=input("Enter the color of your car")
model=input("Enter model of your car")
Battery_size=int(input("Enter Battery Size of car :"))
my_car= car(color,model)
print("Information ABout Car")
my_car.display_info()

my_ecar=ElectricCar(color="Blue",model="Tesla",Battery_size=500)
print("Information about Electric Car")
my_ecar.display_info()


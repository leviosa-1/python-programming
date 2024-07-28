class programmer :
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    
    def get_info(self):
        print(f"Name : {self.name} \n age : {self.age} \n salary: {self.salary}")
        
e1=programmer("Ayush Jaiswal",25,50000)
e2=programmer("Pranjal Dayya",24,48500)
e1.get_info()
e2.get_info()

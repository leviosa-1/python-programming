class Employee :
    def  __init__(self,name,sal):
        self.name=name
        self.sal=sal
    
    def get_sal(self):
        return self
    
e1=Employee("Ayush jaiswal", "920000")
print("Salary :"+e1.sal)
print("Employee name "+e1.name)

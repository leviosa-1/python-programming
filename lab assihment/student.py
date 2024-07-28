class student :
    total_student=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        student.total_student +=1
        
    def student_info(self):
        print(f"Student Name : {self.name} \n Age : {self.age}")
      
    @classmethod   
    def show_total(self):
        print(f"Total Students : {self.total_student}")
        
s1=student("Anurag Solanki",19)
s2=student("Aaditi Barod",20)
s3=student("Kajal Bharti",20)

s1.student_info()
s2.student_info()
s3.student_info()

student.show_total()

class father:
    def __init__(self,fname):
        self.fname=fname
    def fhobbies(self):
        print(f"FAther name : {self.fname}")
        print(f"Likes to Play football  and likes to read books")
        
class mother:
    def __init__(self,mname):
        self.mname=mname
    def mhobbies(self):
        print(f"Mothers name : {self.mname}")
        print("Like to listen music and coocking food")

class child(father or mother):
    def __init__(self,fname,mname,name):
        father.__init__(self,fname)
        mother.__init__(self,mname)
        self.name=name
    def hobbies(self):
        father.fhobbies(self)
        mother.mhobbies(self)
        print(f"My name is : {self.name}")
        print("i like to sing music , playing cricket, and learning new things")
        
c=child(fname="Dinesh Jaiswal",mname= "Savitri Jaiswal", name="Ayush Jaiswal")
c.hobbies() 
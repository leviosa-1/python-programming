name="Ayush jaiswal"
print(name.find('j'))
print(name.replace("Ayush jaiswal","Anurag Solanki"))
print('n' in name)

def lettergenerator(name,date):
    st=f"Hello mam , this is {name} , i will not come on {date}"
    print(st)
    
lettergenerator("Ayush jaiswal", "16th june 2023")

def avg(a,b):
    return (a+b)/2

print(avg(10,50))

try:
    a=int(input("enter your number:"))
    print(a+3)
except Exception as e :
    print("Some error occured ", e)
digit=int(input("enter digit"))
value=int(input("ennter the single value you want to search in digit"))
c=0
string=str(digit)
for char in string:
    if char==str(value):
        c=c+1
        
print(f"{value} found {c} times in {digit}") 
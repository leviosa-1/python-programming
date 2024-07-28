v=['a','e','i','o','u',]
s=input("ENter string")
c=0
for i in s:
    if i.isalpha():
        if i in v:
            c=c+1
        
print(c)


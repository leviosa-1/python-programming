s=input("enter a string :")
print("length of string :",len(s))
print(s.capitalize())
s1=s[0:5]
print(s1)
print(s.endswith("ush"))
print(s.find("a"))
print(s.format(s))

#count vowels inn string
v=('a','A','e','E','i','I','o','O','u','U')
c=0
for char in s :
    if char in v :
        c=c+1
        
print("Vowels in given string is :" , c)

listen 
silent

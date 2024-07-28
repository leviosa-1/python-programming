#write a prog which takes the string as input and show number of lowercase , digit, 
# upper case ,, alphanumeric present in strig 
s=input("Enter a string")
l=u=d=a=0
for i in range(len(s)):
    if(s[i].islower()):
        l=l+1
    if(s[i].isupper()):
        u=u+1
    if(s[i].isdigit()):
        d=d+1
    if(s[i].isalnum()):
        a=a+1
    
print("Number of Lowercase in string :",l)
print("NUmber of uppercase in string is :",u)
print("Number of digits in string is ",d)
print("Number of alphanumeric in string is ",a)
print("Total length of String is ", len(s))


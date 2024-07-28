s1=input()
s2=s1[::-1]
if(s1==s2):
    print('palindrome')
else :
    print("not palindrome")

    
    # print fibonacci uusing list till 9 elements
  
l=[1,1]
for i in range(8):
    l.append(l[i]+l[i+1])
print(l)

    
#check number is in valid formate or not 
#702-489-6018
st=input()
v=True
if(len(st)!=12):
    v=False
if(st[3]!='-' or st[7]!='-'):
    v=False
for i in range(12) :
    if(i==3 or i==7) :
        continue
    if(not(st[i].isdigit())) :
        v=False
print(v)
    
    

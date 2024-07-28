nums=[]
found = False
n=int(input("Enter the size of list:"))
print("Enter the"+str(n)+"Elements of list")
for i in range(n):
    nums.insert(i,int(input()))
print("Given list :",nums) 
key=int(input("Enter the element you want to search in list"))
l=0
u=n
c=0
while(l<=u and found==False):
    m=(l+u)//2
    if(nums[m]==key):
          found=True
    elif(key>=nums[m]):
          l=m+1
    elif(key<=nums[m]):
          u=m-1
    else:
     found=True
    c=c+1
print("Itrations :",c)
if found :
    print("Element Found !!")
else :
    print("Element not FOund !!")
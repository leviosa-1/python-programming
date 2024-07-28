nums=[]
n=int(input("Enter the size of list:"))
print("Enter the"+str(n)+"Elements of list")
for i in range(n):
    nums.insert(i,int(input()))
print("Given list :",nums) 
key=int(input("Enter the element you want to search in list"))
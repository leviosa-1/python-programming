nums=[]
n=int(input("Enter the size of list:"))
print("Enter the"+str(n)+"Elements of list")
for i in range(n):
    nums.insert(i,int(input()))
print("Given list :",nums) 
key=int(input("Enter the element you want to search in list"))
for i in range(n):
      if (nums[i]==key):
          found = True
if found :
    print("Element found!!")
else:
    print("Element Not found!!")
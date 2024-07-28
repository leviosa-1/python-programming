nums=[]
n=int(input("Enter the size of list:"))
print("Enter the"+str(n)+"Elements of list")
for i in range(n):
    nums.insert(i,int(input()))
print("unsorted list :",nums)       
for i in range(n):
    for j in range(n-i-1):
          if(nums[j]>nums[j+1]):
              nums[j],nums[j+1]=nums[j+1],nums[j]
              
print("sorted list :",nums)      
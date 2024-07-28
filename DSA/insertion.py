nums=[]
n=int(input("Enter the size of list:"))
print("Enter the "+str(n)+" elements of list")
for i in range(n):
    nums.insert(i,int(input()))

for i in range(n):
    current=nums[i]
    j=i-1
    while nums[j]>current and j>=0:
        nums[j+1]=nums[j]
        j=j-1
    else:
        nums[j+1]=current
print("Sorted list :",nums)
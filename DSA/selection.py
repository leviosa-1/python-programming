nums=[]
n=int(input("Enter the size of list:"))
print("Enter the"+str(n)+"Elements of list")
for i in range(n):
    nums.insert(i,int(input()))
print("unsorted list :",nums)  
# selectio sort algorithm
for i in range(n):
    min_index=i
    for j in range(i+1,n):
        if(nums[j]<nums[min_index]):
            min_index=j
    nums[i],nums[min_index]=nums[min_index],nums[i]
        
print("Sorted List :",nums)
        
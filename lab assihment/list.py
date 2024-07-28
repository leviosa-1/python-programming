lst=input("Enter elements:").split()
nums=[int(num) for num in lst]
if not nums :
    print("Enter atlest one number")
print(lst)
max1=max(nums)
min1=min(nums)
print(max1)
print(min1)
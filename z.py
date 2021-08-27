arr=[]
nums=[5,3,4,2,1]
for i in range(len(nums)):
    print(nums)
    arr.append(min(nums))
    nums.remove(min(nums))
    print(nums)
print(arr)
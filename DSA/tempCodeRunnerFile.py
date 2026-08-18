nums = [0,1,0,3,4,0,5,6,0,9]
k=0
for i in range(len(nums)):
    if(nums[i] !=0):
        nums[k]=nums[i]
        k+=1
print(nums)
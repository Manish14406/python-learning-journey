
k = 1
nums = [1,2,3,3,4,4]
for i in range(1, len(nums)):
    if nums[i] != nums[i - 1]:
      nums[k] = nums[i]
      k += 1

print(k)
       

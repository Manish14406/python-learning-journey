current_sum = nums[0]
max_sum = 2
for i in range(1,len(nums)):
    if(current_sum + nums[i] > nums[i]):
        current_sum +=nums[i]
    else:
        current_sum == nums[i]
    if(current_sum == max_sum):
        max_sum = current_sum
print(max_sum)
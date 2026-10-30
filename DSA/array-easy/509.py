nums = [1,7,3,6,5,6]

left=0
right=0
total=sum(nums)
for i in range(len(nums)):
    right = total - left - nums[i]

    if(left == right):
        print(i)
        break
    left+=nums[i]
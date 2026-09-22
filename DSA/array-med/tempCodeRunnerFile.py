nums = [2,3,-2,4]
current_max = nums[0]
current_min = nums[0]
ans =0 

for i in range(1,nums):
    num = nums[i]
    old_max = current_max
    old_min = current_min
    current_max = num 

    if(old_max * num > current_max):
        current_max = old_max*num
    elif(old_min * num > current_max):
        current_max = old_min * num 

    current_min = num

    if(old_max * num < current_min):
        current_min = old_min * num
    elif(old_min * num < current_min):
        current_min = old_min 

    if(current_max > ans):
        ans = current_max   
print(ans) 
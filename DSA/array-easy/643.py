# max avg of a window k 
nums = [-1]
k = 1
left=0
total=0
max_avg = -10000
for right in range(len(nums)):
    total+=nums[right]
    if(right - left + 1 ==k):
        avg = total/k
        if(avg > max_avg):
            max_avg = avg
        total-=nums[left]
        left+=1
print(max_avg)

# Maximum sum of the possible subarray from the given array

#Brute force approach
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# for start in range(len(nums)):
#     current_sum = 0
#     for end in range(start,len(nums)):
#         current_sum += nums[end]
        
# Kadans algorithm optimal approach
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# current_sum = nums[0]
# max_sum = nums[0]
# for i in range(len(nums)):
#     if(current_sum + nums[i] > nums[i]):
#         current_sum +=nums[i]
#     else:
#         current_sum = nums[i]
#     if(current_sum > max_sum):
#         max_sum = current_sum
# print(max_sum)

# max subarray with its elements 
# nums =  [5,4,-1,7,8]
# current_sum = nums[0]
# max_sum = nums[0]

# current_start = 0
# best_start = 0
# best_end = 0

# for i in range(1,len(nums)):
#     if(current_sum + nums[i] > nums[i]):
#         current_sum +=nums[i]
#     else:
#         current_sum = nums[i]
#         current_start = i

#     if(current_sum > max_sum):
#         max_sum = current_sum
#         best_start = current_start
#         best_end = i
# print(nums[best_start:best_end+1])
    

# max product of sub array 

nums = [2,3,-2,4]
current_max = nums[0]
current_min = nums[0]
ans =0 

for i in range(1,len(nums)):
    num = nums[i]
    old_max = current_max
    old_min = current_min
    current_max = num 

    if(old_max * num > current_max):
        current_max = old_max*num
    if(old_min * num > current_max):
        current_max = old_min * num 

    current_min = num

    if(old_max * num < current_min):
        current_min = old_min * num
    if(old_min * num < current_min):
        current_min = old_min * num 

    if(current_max > ans):
        ans = current_max   
print(ans) 
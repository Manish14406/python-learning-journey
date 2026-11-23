nums = [0,3,7,2,5,8,4,6,0,1]

num_set = set(nums)
longest=0
for num in nums:

    if(num-1 not in num_set):
        current_num = num
        current_len=1
        while(current_num+1 in num_set):
            current_num +=1
            current_len+=1
        if(current_len > longest):
            longest=current_len
print(longest)

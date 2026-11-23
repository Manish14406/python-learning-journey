nums =   [2, 4, 3, 2, 5, 4] 

freq={}
i=0
max_freq=0
for i in range(len(nums)):
    if(nums[i] in freq):
        freq[nums[i]]+=1
    else:
        freq[nums[i]]=1
    if(freq[nums[i]] > max_freq):
        max_freq=nums[i]

print(max_freq)
    
freq ={0:0,1:0,2:0}
nums = [2,0,2,1,1,0]


for num in nums:
    if(num in freq):
        freq[num] +=1

i=0

while(freq[0] > 0):
    nums[i]=0
    i+=1
    freq[0]-=1

while(freq[1] > 0):
    nums[i] =1
    i+=1
    freq[1]-=1

while(freq[2] > 0):
    nums[i] =2
    i+=1
    freq[2]-=1
print(nums)
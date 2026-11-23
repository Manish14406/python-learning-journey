nums = [1,2,3,2]

freq={}
for i in range(len(nums)):
    if(nums[i] in freq):
        freq[nums[i]]+=1
    else:
        freq[nums[i]]=1
seen=set()
print(freq)
for key,value in freq.items():
    if(freq[value] == 1):
        seen.add(key)
s=sum(seen)
print(s)

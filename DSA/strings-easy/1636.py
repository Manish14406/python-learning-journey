freq={}
l=[]
nums = [1,1,2,2,2,3]
element=0
nums.sort(reverse=True)
for i in range(len(nums)):
    if(nums[i] in freq):
        freq[nums[i]]+=1
    else:
        freq[nums[i]]=1

while freq:
    element=min(freq,key=freq.get)
    l.extend([element] * freq[element])
    del freq[element]
print(l)
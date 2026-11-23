nums = [1,1,1,2,2,3]
k=2
freq={}
max_freq=0
element=0
l=[]
for i in range(len(nums)):
        if(nums[i] in freq):
            freq[nums[i]]+=1
        else:
            freq[nums[i]]=1
i=0
while(i<k):
     element=max(freq, key=freq.get)
     l.append(element)
     del freq[element]
     i+=1
print(l)
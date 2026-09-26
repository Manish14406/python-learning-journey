strs = ["eat","tea","tan","ate","nat","bat"]
freq1={}
freq2={}

for i in range(len(strs)):
    if(strs[i] in freq1):
        freq1[strs[i]]=1
    for j in range(i+1,len(strs)):
        if(strs[j]  in freq2):
            freq2[strs[j]]=1
        else: freq2[strs[j]]+=1
print(freq1)
print(freq2)

    
    

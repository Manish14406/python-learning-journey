arr = [2,2,3,4]

freq={}
for i in range(len(arr)):
    if(arr[i] in freq):
        freq[arr[i]]+=1
    else:
        freq[arr[i]]=1
l=[]
        
for key,value in freq.items():
    if(key == value):
        l.append(key)
s = max(l)
print(s)

arr = [1,2,2,1,1,3]
freq={}

for i in range(len(arr)):
    if(arr[i] in freq):
        freq[arr[i]]+=1
    else:
        freq[arr[i]]=1
print(freq)


# iterate using set and seen 

seen = set()

for values in freq.values():
    if(values in seen):
        print("Duplicate found")
    else:
        seen.add(values)

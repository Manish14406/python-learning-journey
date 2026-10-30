nums = [8,1,2,2,3]
sorted_arr = sorted(nums)

count ={}
i=0
while(i<len(sorted_arr)):
    if(sorted_arr[i] not in count):
        count[sorted_arr[i]] = i
    i+=1
ans = []
for num in nums:
    ans.append(count[num])

print(ans)
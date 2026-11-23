nums = [1,2,3]
k=3
seen ={0:1}
prefix_sum=0
count=0

for i in range(len(nums)):
    prefix_sum+=nums[i]

    need = prefix_sum - k

    frequency = seen.get(need,0)
    count +=frequency

    frequency = seen.get(prefix_sum,0)
    frequency+=1
    seen[prefix_sum]=frequency
print(count)
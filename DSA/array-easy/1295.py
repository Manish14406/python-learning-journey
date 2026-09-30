nums = [12,345,2,6,7896]
# l=[0,2,4,6,8]
# count=0
# for i in range(len(nums)):
#     if(len(str(nums[i])) in l):
#         count+=1
# print(count)
count=0
for num in nums:
    digits_count=0
    while(num>0):
        digits = num % 10
        digits_count+=1
        num = num//10
    if(digits_count % 2 == 0):
        count+=1
print(count)
    

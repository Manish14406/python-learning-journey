# arr = [1,2,3,4,5]
# lar = arr[0]
# sec_lar= arr[1]

# for i in range(len(arr)):
#     if(arr[i]> lar):
#         sec_lar = lar
#         lar = arr[i]
#     elif(lar > sec_lar and sec_lar!=lar):
#         sec_lar = arr[i]
# print(sec_lar)

nums = [-2,1,-3,4,-1,2,1,-5,4]

current_sum = nums[0]
max = nums[0]

for i in range(1,len(nums)):
    if(current_sum + nums[i] > nums[i]):
        current_sum +=nums[i]
    else :
        current_sum = nums[i] 
    if(current_sum > max ):
        max = current_sum
print(max)
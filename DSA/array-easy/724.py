nums = [1,7,3,6,5,6]

left=0
beg=nums[0]
end=len(nums)-1
right =len(nums)-1
while(left<right):
    beg=beg+nums[right]
    end=end+nums[left]
    if(beg == end):
        print(beg,end)
        break
    left+=1
    right-=1
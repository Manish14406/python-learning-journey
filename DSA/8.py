# 2 pointer problems
# k = 1
# nums = [1,2,3,3,4,4]
# for i in range(1, len(nums)):
#     if nums[i] != nums[i - 1]:
#       nums[k] = nums[i]
#       k += 1

# print(k)


# 2 pointer solution to put the zero to end and also non zeros numbers at the beginning 
# nums = [0,1,0,3,4,0,5,6,0,9]
# k=0
# for i in range(len(nums)):
#     if(nums[i] !=0):
#         nums[k]=nums[i]
#         k+=1
# print(nums)

# while(k <len(nums)):
#     nums[k] = 0
#     k+=1
# print(nums)


#remove duplicate in the sorted array
# nums = [1,1,2,2,3,3,4,4,5]
# k=1
# for i in range(1,len(nums)):
#     if(nums[i] != nums[i-1]):
#         nums[k] = nums[i]
#         k+=1
# print(nums[:k])
        

# reverse an array
# nums = [1,2,3,4,5]
# k=len(nums)
# i=0
# while(i!=k):
#     (k,i)=(i,k)
#     i+=1
# print(nums)

# palindrome in two pointer approach
# s = "madam"
# left = 0
# right = len(s)-1
# while(left<right):
#     if(s[left]!=s[right]):
#         print(False)
#         break
#     left +=1
#     right -=1
# else:print(True)

 # Find two numbers whose sum=10
# nums = [1,2,3,4,6,8]
# left =0
# right = len(nums)-1
# while(left < right):
#     target = nums[left] + nums[right ]

#     if target < 10:
#         left +=1
#     elif target > 10:
#         right-=1
#     else : 
#         print(nums[left],nums[right])
#         left +=1
#         right -=1

nums = [2,7,11,15]
left = 0
right = len(nums)-1
while(left < right):
    target = nums[left]  + nums[right]

    if(target < 9):
        left+=1
    elif(target > 9):
        right-=1

    else:
      print(nums[left],nums[right])
      left+=1
      right-=1


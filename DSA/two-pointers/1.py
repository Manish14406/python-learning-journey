# arr = [0, 1, 0, 3, 12]

# left =0
# right =0
# for right in range(len(arr)):
#     if(arr[right]!=0):
#         arr[right],arr[left] = arr[left],arr[right]
#         left+=1

# print(arr)

# sums


arr=[2, 4, 5, 7, 9, 11, 14]
target = 16
left = 0
right = len(arr)-1
while(left<right):
    total = arr[left]+ arr[right]

    if(total==target):
        print(left,right)
        break
    elif(total < target):
        left+=1
    elif(total > target):
        right-=1

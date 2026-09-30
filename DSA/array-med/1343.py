arr = [11,13,17,23,29,31,7,5,2,3]   
k = 3
threshold = 5
left = 0
count=0
total=0
for right in range(len(arr)):
    total+=arr[right]
    if(right - left +1 == k):
        avg = total / k
        if(avg >=threshold):
            count+=1
        total-=arr[left]
        left+=1
print(count)


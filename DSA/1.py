arr = [3,4,5,6]

largest = arr[0]

for i in range(len(arr)):
    if(arr[i]>largest):
        largest = arr[i]

print(largest)
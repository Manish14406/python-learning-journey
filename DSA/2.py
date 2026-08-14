arr=[2,1,3,4]

breaks = 0
for i in range(len(arr)):
    if(arr[i] > arr[(i+1)%len(arr)]):
        breaks+=1
if(breaks <=1):
    print("true")
else:
    print("false")
        
   

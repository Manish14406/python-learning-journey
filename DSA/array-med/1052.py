customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
minutes = 3

left = 0
sums = 0
suma=0
max=0
for right in range(len(customers)):
    if(grumpy[right]==0):
        sums = sums + customers[right]

    if(right-left + 1 == minutes):
        for i in range(left,right):
            if(grumpy[left] == 1):
                suma = suma + customers[left]
        if(suma > max):
            max = suma
        left+=1
print(sums+max)



num = 38
sums = 0
while(num >=10):
    sums=0
    while(num>0):
        digits = num%10
        sums = sums + digits
        num = num // 10
    num = sums 
print(sums)
    

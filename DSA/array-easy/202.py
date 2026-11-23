n = 19
sums = 0
seen = set()

while(n!=1):
    if(n in seen):
        print(False)
        break
    seen.add(n)
    sums=0
    while(n!=0):
        digit = n%10
        sums = sums + digit*digit
        n = n//10

    
version1 = "1.2"
version2 = "1.10"


v1 = list(map(int, version1.split(".")))
v2 = list(map(int, version2.split(".")))


n = max(len(v1),len(v2))

for i in range(n):
    if(i < len(v1)):
        num1 = v1[i]
    else: 0
    if(i < len(v2)):
        num2 = v2[i]
    else : 0

    if(num1 > num2):
        print(1)
    elif(num1 < num2):
        print(2)
    
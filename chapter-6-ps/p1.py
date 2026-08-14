a = int(input("Enter 1 :\n"))
c = int(input("Enter 2 :\n"))
d = int(input("Enter 3 :\n"))
e = int(input("Enter 4 :\n"))

if(a>c and a>d and a>e):
    print(f"{a} is greatest")
elif(c>a and c>d and c>e):
     print(f"{c} number is greatest")
elif(d>a and d>c and d>e):
     print(f"{d} number is greatest")
else:
     print(f"{e} number is greatest")

     



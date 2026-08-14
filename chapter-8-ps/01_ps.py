# def funct(a,b,c):
#     if(a>b and a>c):
#         print(f"{a} is greater")
#     elif(b>a and b>c):
#         print(f"{b} is greater")
#     else:
#         print(f"{c} is greater")

# a = int(input("Enter :"))
# b = int(input("Enter :"))
# c = int(input("Enter :"))

# funct(a,b,c)

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    
a = 1
b = 2
c = 3

print(greatest(a,b,c))
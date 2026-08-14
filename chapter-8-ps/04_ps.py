# def natural(n):
#     i = 1
#     sum = 0
#     while(i<=n):
#         sum = sum + i
#         i+=1
#     return sum
    
# n = int(input("Enter number : "))
# a = natural(n)

# print(f"Sum : {natural(n)}")


# Recurssive

'''
sum(1)= 1
sum(5)= 1+2+3+4+5
sum(n) = n, n+1,.......n-1 +1
'''

def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+n

n = int(input("Enter : "))
print(sum(n))
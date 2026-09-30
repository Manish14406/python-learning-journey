n = 234

# strs = str(n)
# sums=0
# multiply=1
# for  i in range(len(strs)):
#     sums = sums + int(strs[i])
#     multiply = multiply * int(strs[i])
# print(multiply-sums)

multiply = 1
sums = 0
while n > 0:
    digits = n%10
    sums+=digits
    multiply*=digits
    n = n//10
print(multiply-sums)
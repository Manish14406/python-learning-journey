# string to integer 
i=0
nums=0
num = "134aaaaad"
while(i < len(num) and num[i].isdigit()):
    nums = nums * 10 + int(num[i])
    i+=1
print(nums)
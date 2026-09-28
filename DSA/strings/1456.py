# s = "abciiidef"
# k=3
# left=0
# for right in range(len(s)):
#     if(right - left + 1>k ):
#         left+=1
        
#sliding window 
s = "abciiidef"
left = 0
k = 3
count=0
count_max=0
for right in range(len(s)):
    if(s[right] in "aeiou"):
        count+=1
    if(right-left + 1 == k):
        if(count > count_max):
            count_max =count
        if(s[left] in "aeiou"):
            count-=1
        left+=1
print(count_max)
        
haystack = "mississippi"
needle = "issip"
k = len(needle)

left = 0
if(haystack == needle):
    print(0)
if(len(needle) == 1):
    for i in range(len(haystack)):
        if(needle in haystack[i]):
            print(i)

for right in range(1,len(haystack)):
    if(right - left + 1 >= k):
        str = haystack[left:right+1]
        print(str)
        if(needle == str):
            print(haystack.index(str))
            break
        left+=1

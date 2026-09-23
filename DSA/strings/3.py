# this problem is the combination of sliding window and set 
s = "abcabcbb"

char = set()
left = 0
max_len = 0

for right in range(len(s)):
    if(s[right] in char):
        char.remove(s[right])
        left+=1
    char.add(s[right])
    current_len = right -left+1
    if(current_len > max_len):
        max_len = current_len
print(max_len)
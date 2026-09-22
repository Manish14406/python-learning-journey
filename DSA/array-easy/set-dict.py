# Intersection of two arrays   (set)
# nums1 = [1,2,2,1]
# nums2=[2,2]
# num1 = set(nums1)
# l2=set()

# for i in range(len(nums2)):
#     if(nums2[i] in num1):
#         l2.add(nums2[i])
# print(l2)

# problem strings:
s = "saw-42"
s1=[]
s2=[]
for i in range(len(s)):
    s1.append(s[i])

for i in range(len(s1)):
    if not s1[i].isalpha():
        s2.append(s1[i])
s3 = "".join(s2)
print(s3)



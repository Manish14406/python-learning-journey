# arr = [3, 5, 3, 2, 5, 3]
# freq={}
# for num in arr:
#     if(num in freq):
#         freq[num]+=1
#     else:
#         freq[num]=1
# print(freq)



# arr = [4, 2, 4, 3, 2, 7, 3]
# freq={}
# for num in arr:
#     if(num in freq):
#         freq[num]+=1
#     else:
#         freq[num]=1

# for num in freq:
#     if(freq[num] ==1):
#         print(num)
#         break

# arr = [2, 4, 2, 5, 4, 6, 2, 5]

# freq={}
# for num in arr:
#     if(num in freq):
#         freq[num] +=1
#     else:
#         freq[num]=1
# for num in freq:
#     if(freq[num] > 1):
#         print(num)

# arr = [1, 3, 2, 3, 4, 1, 3, 2]

# freq={}
# for num in arr:
#     if(num in freq):
#         freq[num] +=1
#     else:
#         freq[num]=1
# print(freq)
# max_freq=0
# number=0
# for num in freq:
#     if(freq[num] > max_freq):
#         max_freq = freq[num]
#         number=num
# print(max_freq)
# print(number)

# arr = [1, 2, 2, 3, 3, 3, 4, 4]
# k = 2
# freq={}
# for num in arr:
#     if(num in freq):
#         freq[num] +=1
#     else:
#         freq[num]=1
# for num in freq:
#     if(freq[num] ==2):
#         print(num)

# arr = [5, 3, 4, 3, 5, 2]

# freq={}
# for num in arr:
#     if(num in freq):
#         freq[num]+=1
#     else:
#         freq[num]=1

# for num in arr:
#     if(freq[num] > 1):
#         print(num)
#         break

# arr = [4, 1, 7, 3, 8, 2]
# target = 10 

# seen ={}
# for i in range(len(arr)):
#     if(target - arr[i] in seen):
#         print(seen[arr[i]])
#     else:
#         seen[arr[i]] = i

l1 = ['manish','ruthik','anni']
l2=['havya','kamali','chikku']
j=0
dict={}
for i in range(len(l1)):
    dict[l1[i]] = l2[j]
    j+=1
print(dict)


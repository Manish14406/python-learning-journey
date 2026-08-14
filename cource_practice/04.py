# list = ["apple","banana","cherry"]
# # print(list[0])
# # list.remove("banana")
# # list.insert(1,"orange")
# # print(li

# l =[]

# for i in range(11):
#     l.append(i)
# print(l)
# print(l[1:4])
# # print(l[6:11])

# l = [5,2,9,1,7]
# print(l.sort())

# l.append(10)
# print(l)

# set1 = {1,2,3}
# set2 = {3,4,5}

# print(set1.intersection(set2))
# print(set1.union(set2))
# print(set1.difference(set2))
import pandas as pd
dict = {
    "manish":23,
    "havya" : 283,
    "superman" : 733
}

dicy = pd.Series(dict)
print(dicy)

for keys,values in dict.items():
    print(keys,values)



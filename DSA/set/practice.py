arr = list(map(int,input().split()))

s= set(arr)

so = sorted(s)

l = list(so)

print(l[len(so)-2])
arr = [12,39,9,67,3,90,100,121,400,800]

lar = arr[0]

for i in range(len(arr)):
    if(arr[i] > lar):
        lar = arr[i]
print(lar)
sec_lar = arr[1]
for i in range(len(arr)):
    if(lar > arr[i] and arr[i] > sec_lar):
        sec_lar = arr[i]        
print(sec_lar)

arr = [1,2,3,4,5]
lar = arr[0]
sec_lar= arr[1]

for i in range(len(arr)):
    if(arr[i]> lar):
        sec_lar = lar
        lar = arr[i]
    elif(lar > sec_lar and sec_lar!=lar):
        sec_lar = arr[i]
print(sec_lar)
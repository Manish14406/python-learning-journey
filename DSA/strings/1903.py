# # largest odd number in a string string this is of single digit 
# num = "426035"
# ls=[]
# max=0
# for i in range(len(num)):
#     if(int(num[i]) % 2 !=0):
#         ls.append(num[i])
#         if(int(num[i]) > max):
#             max = int(num[i])
# print(max)

# to find the overall largest odd number in a string 
num = "242626242420000000000"
l=[]
for i in range(len(num)-1,-1,-1):
    if(int(num[i]) % 2 != 0):
        l.append(num[:i+1])
        break
print("".join(l))
           



            

            
        

   
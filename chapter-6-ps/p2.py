s1 = int(input("Enter the marks of sub1 :"))
s2 = int(input("Enter the marks of sub2 :"))
s3 = int(input("Enter the marks of sub3 :"))

marks = s1+s2+s3
s1 = (s1/100)*100
s2 = (s2/100)*100
s3 = (s3/100)*100
p = ((s1+s2+s3)/300)*100

# if(p>40):
#     if(s1>33):
#         if(s2>33):
#             if(s3>33):
#                 print("The student have finally passed\n")
# else:
#     print("The student failed\n") 
# print(f"The overall percentage of the student is {p}%:")               

if(marks >=40 and s1>33 and s2>33 and s3>33):
    print("The student has passed\n")
else:
    print("The student has failed\n")

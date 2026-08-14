n = int(input("Enter a number to check the given number is prime or not :"))
i =0
for i in range(2,n):
    if(n%i) == 0:
        print("The given number is not a prime \n")
        break
else:
    print("PRIMEEEE")
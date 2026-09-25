# ok now I understood the logic 
digits = [1,9,9]

for i in range(len(digits)-1,-1,-1):
    if(digits[i] < 9):
        digits[i]+=1
        print(digits) # return function 
    digits[i] = 0
print([1] + digits) # return function 
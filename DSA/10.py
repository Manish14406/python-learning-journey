prices = [7,6,4,3,1]
min = 0
for i in range(len(prices)):
    for j in range(i+1,len(prices)):
        if(prices[i] < prices[j]  and prices[i]< min) :
            min = prices[j] - prices[i]
print(min)
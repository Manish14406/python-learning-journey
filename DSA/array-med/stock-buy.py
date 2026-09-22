prices = [7, 0, 5, 3, 6, 4]

minimum = prices[0]
max_profit = 0

for i in range(1, len(prices)):
    if prices[i] < minimum:
        minimum = prices[i]
    else:
        profit = prices[i] - minimum

        if profit > max_profit:
            max_profit = profit

print(max_profit)  
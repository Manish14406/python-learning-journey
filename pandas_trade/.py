import pandas as pd

data = [
    ["2025-12-01 10:00", 100.0, 105.0, 99.0, 102.0, 150],
    ["2025-12-01 10:05", 102.0, 103.0, 101.0, 101.0, 200],
    ["2025-12-01 10:10", 101.0, 108.0, 100.0, 107.0, 180],
]
cols = ['time','open','high','low','close','volume']
df = pd.DataFrame(data, columns=cols)
print(df)

#print highs / get whole column
print(df['high'])

#get one full row 
print(df.loc[1])

#get one specific value
print(df.loc[1,'high'])

#looping concept  / prints each candles high with its index
for i in range(len(df)):
    print("Candle",i,"High =",df.loc[i,"high"])

#Now comes major liquidity part looping with previous / current /next - candle

for j in range(1,len(df)-1):  # avoids first and last candles 
    prev_high = df.loc[j-1,'high']
    curr = df.loc[j,'high']
    next = df.loc[j+1,"high"]
    print(f"Index : {j} previous high = {prev_high} current = {curr}  next-candle={next}")

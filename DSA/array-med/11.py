height = [1,8,6,2,5,4,8,3,7]
multi=1
great=0
for i in range(len(height)):
    multi = multi * height[i]
    if(multi > great):
        great = multi
print(great)
   
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = int(input("enter : "))
for i in range(len(matrix)):
    for j in range(i+1,len(matrix)):
        if(matrix[i][j] == target):
            print(matrix[i][j])
def kadene(arr):
    max_sum=float('-inf')
    current_sum=0
    for num in arr:
        current_sum=max(num,current_sum+num)
        max_sum=max(max_sum,current_sum)
    return max_sum
def submatrix(matrix):
    row=len(matrix)
    col=len(matrix[0])
    max_sum=float('-inf')
    for left in range(col):
        temp=[0]*row
        for right in range(left,col):
            for i in range(row):
                temp[i]+=matrix[i][right]
            current_max=kadene(temp)
            max_sum=max(max_sum,current_max)
    return max_sum
matrix=[[1,2,5],[3,4,6],[7,8,9]]
print(submatrix(matrix))            
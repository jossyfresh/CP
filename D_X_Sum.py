
def diagonalSum(i, j , matrix):
    sum = 0
    row = len(matrix)
    col = len(matrix[0])
    k, l = i, j
    while i < row and j >= 0:
        sum+=matrix[i][j]
        i += 1
        j -= 1
    sum-=matrix[k][l]
    i , j = k , l
    while i < row and j < col:
        sum+=matrix[i][j]
        i += 1
        j += 1
    sum-=matrix[k][l]
    i, j = k ,l
    while i >= 0 and j >= 0:
        sum += matrix[i][j]
        i -= 1
        j -= 1
    sum-=matrix[k][l]
    i, j = k, l
    while i >= 0 and j < col:
        sum+=matrix[i][j]
        i -= 1
        j += 1
    sum-=matrix[k][l]
    return sum+matrix[k][l]
t = int(input())
for i in range(t):
    nm = list(map(int,input().split()))
    nums = []
    for i in range(nm[0]):
        nums.append(list(map(int,input().split())))
    maximum = 0
    for i in range(nm[0]):
        for j in range(nm[1]):
            maximum = max(maximum,diagonalSum(i,j,nums))
    print(maximum)
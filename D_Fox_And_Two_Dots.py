from collections import deque
n,m = map(int,input().split())
matrix = []
for _ in range(n):
    mat = input()
    matrix.append(mat)
def inbound(row, col):
    return (0 <= row < len(matrix) and 0 <= col < len(matrix[0]))
direction = [(0, 1), (1, 0),(0, -1), (-1, 0)]
flag = [0]
visited = set()


def dfs(node,parent,color):
    visited.add(node)
    i,j = node
    for x,y in direction:
        child = (x+i,y+j)
        if inbound(x+i,y+j) and matrix[x+i][y+j] == color:
            if child in visited and child != parent:
                flag[0] = 1
                return 
            if child not in visited:
                dfs(child,node,color)

                
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        node = (i,j)
        if node not in visited:
            color = matrix[i][j]
            dfs(node,-1,color)

if flag[0]:
    print("Yes")
else:
    print("No")


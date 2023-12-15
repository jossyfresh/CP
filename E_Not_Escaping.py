t =  int(input())
for _ in range(t):
    n,m,k = map(int,input().split())
    x = list(map(int,input().split()))
    array = []
    for _ in range(k):
        array.append(list(map(int,input().split())))
    dist = {}
    edges = []
    for i in range(n):
        for j in range(m):
            dist[(i,j)] = float("inf")
            if j+1 < m:
                edges.append([i,j,i,j+1,x[i]])
    print(edges)
# 0902380202 
# Natnael Tafese
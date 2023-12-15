import heapq
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    heapq.heapify(a)
    for i in range(len(b)):
        heapq.heapreplace(a, b[i])
    print(sum(a))

    
            
    
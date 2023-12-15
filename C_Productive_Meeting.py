import heapq
t = int(input())
for _ in range(t):
    n = int(input())
    num = list(map(int,input().split()))
    b = []
    for i in range(len(num)):
        num[i] = [-num[i],i]
    heapq.heapify(num)
    ans = []
    while len(num) > 1:
        mx,inmx = heapq.heappop(num)
        mx *= -1
        mn,inmn  = heapq.heappop(num)
        mn *= -1
        if mx == 0 or mn == 0:
            break
        ans.append((inmn+1,inmx+1))
        heapq.heappush(num,[-(mx-1),inmx])
        heapq.heappush(num,[-(mn-1),inmn])
    print(len(ans))
    for x in ans:
        print(*x)

  

        
        



    
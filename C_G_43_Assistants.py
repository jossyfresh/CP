import heapq
t = int(input())
for _ in range(t):
    n = int(input())
    time =  []
    for _ in range(n):
        x,y = map(int,input().split())
        time.append([x,y])
    time.sort()
    heap = []
    max_ = 0
    heapq.heapify(heap)
    for x in time:
        if not heap:
            heap.append(x[1])
        else:
            if heap[0] <= x[0]:
                heapq.heappop(heap)
                heapq.heappush(heap,x[1])
            else:
                heapq.heappush(heap,x[1])
        max_ = max(max_,len(heap))
    print(max_)
    
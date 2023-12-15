from collections import Counter
from itertools import combinations
import heapq
n,k = map(int,input().split())
s =  list(map(int,input().split()))
count = Counter(s)
count = sorted(count.items(),key = lambda x:x[1],reverse = True )
ans = []
ans2 = []
for i in range(k):
    x = count[i]
    ans.append((x[1],x[0]))
    ans2.append((-(x[1]),x[0]))
heapq.heapify(ans)
heapq.heapify(ans2)
print(ans)
print(ans2)

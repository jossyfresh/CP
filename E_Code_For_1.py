import heapq
n,l,r = map(int,input().split())
num = [(-n,0)]
heapq.heapify(num)
while abs(num[0][0]) > 1:
    cur,i = heapq.heappop(num)
    cur = abs(cur)
    first =  (-(cur // 2),i-1)
    second = (-(cur % 2),i)
    third = (-(cur // 2),i+1)
    heapq.heappush(num,first)
    heapq.heappush(num,second)
    heapq.heappush(num,third)
num.sort(key=lambda x:x[1])
print(num)
    


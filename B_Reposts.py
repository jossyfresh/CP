from collections import defaultdict
n = int(input())
adjlist = defaultdict(list)
for _ in range(n):
    new,x,old = map(str,input().split())
    new = new.lower()
    old = old.lower()
    adjlist[old].append(new)
queue = ["polycarp"]
ans = 1
while queue:
    n = len(queue)
    while n:
        n-=1
        curr = queue.pop(0)
        for i in adjlist[curr]:
            queue.append(i)
    ans+=1
print(ans-1)

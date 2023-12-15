from collections import Counter,deque,defaultdict
n,m = map(int,input().split())
adjlist = defaultdict(list)
indegree = defaultdict(int)
for _ in range(m):
    x,y = map(int,input().split())
    adjlist[x].append(y)
    adjlist[y].append(x)
    indegree[x] += 1
    indegree[y] += 1
visited = set()
ans = 0
for x in adjlist:
    if x not in visited and indegree[x] == 2:
        queue = deque()
        queue.append(x)
        flag = 0
        while queue:
            n = len(queue)
            while n:
                n -= 1
                cur = queue.popleft()
                visited.add(cur)
                for node in adjlist[cur]:
                    if node not in visited:
                        if indegree[node] != 2:
                            flag = 1
                        queue.append(node)
                        visited.add(node)
        if not flag:
            ans += 1
print(ans)
                
                    

# c = 0
# for x in connected:
#     flag = 0
#     if len(connected[x]) < 3:
#         flag = 1
#         continue
#     for node in connected[x]:
#         if indegree[node] != 2:
#             flag = 1
#             break
#     if not flag:
#         c += 1
# print(c)

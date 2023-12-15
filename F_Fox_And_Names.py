from collections import defaultdict,Counter
from collections import deque
n = int(input())
adjlist = defaultdict(list)
incoming = Counter()
name = []
flag = 0
for _ in range(n):
    x = input()
    name.append(x)
for i in range(len(name)-1):
    first = name[i]
    second = name[i+1]
    f = 0
    for i in range(min(len(first), len(second))):
        if first[i] != second[i]:
            adjlist[first[i]].append(second[i])
            incoming[second[i]] += 1
            f = 1
            break
    if not f and len(first) > len(second):
        flag = 1

ans = []
visited = set()

queue = deque()
for i in range(97,123):
    if chr(i) not in incoming:
        queue.append(chr(i))
while queue:
    x = queue.popleft()
    ans.append(x)
    visited.add(x)
    for node in adjlist[x]:
        if node in visited:
            flag = 1
        if node in incoming:
            incoming[node] -= 1
            if incoming[node] == 0:
                queue.append(node)
                visited.add(node)
res = ""
for i in range(len(ans)):
    res += ans[i]
if len(res) != 26:
    flag = 1
if not flag:
    print(res)
else:
    print("Impossible")

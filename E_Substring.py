import sys
sys.setrecursionlimit(10000)
from collections import defaultdict

n, m = map(int, input().split())
letters = input()
graph = defaultdict(list)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)

max_count = 0
max_letter = '' 

def dfs(node, count, letter):
    global max_count, max_letter
    if count > max_count:
        max_count = count
        max_letter = letter
    
    for nei in graph[node]:
        dfs(nei, count + (letters[nei-1] == letter), letter)

for i in range(1, n+1):
    dfs(i, 1, letters[i-1])

if max_count == n:
    print(-1)
else:
    print(max_count)

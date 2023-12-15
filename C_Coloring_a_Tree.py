import sys,threading
from collections import defaultdict,deque
def main():
    n = int(input())
    adjlist = defaultdict(list)
    a = list(map(int,input().split()))
    c = list(map(int,input().split()))
    maps = {}
    for i in range(len(a)):
        adjlist[a[i]].append(i+2)
        maps[a[i]] = -1
        maps[i+2]  = -1
    ans = 0
    queue = deque()
    queue.append(1)
    visited = set()
    while queue:
        len_ = len(queue)
        while len_:
            len_ -= 1
            cur = queue.popleft()
            visited.add(cur)
            for node in adjlist[cur]:
                if node not in visited:
                    if c[node-1] != c[cur-1]:
                        ans += 1
                    queue.append(node)
    print(ans+1)

sys.setrecursionlimit(1 << 30)

threading.stack_size(1 << 27)

main_thread = threading.Thread(target = main)

main_thread.start()

main_thread.join()
    

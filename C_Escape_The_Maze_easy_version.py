from collections import defaultdict,deque
t =  int(input())
for _ in range(t):
    nothing = input()
    n,k = map(int,input().split())
    adjlist = defaultdict(list)
    fr = list(map(int,input().split()))
    for i in range(n-1):
        x,y = map(int,input().split())
        adjlist[x].append(y)
        adjlist[y].append(x)       
    queue = deque()
    queue.append(1)
    visited = set()
    ans = 0
    level = 0
    flag = 0
    queue = deque()
    for x in fr:
        queue.append(x)
    path = []
    while queue:
        n = len(queue)
        single = set()
        while n:
            n -= 1
            cur = queue.popleft()
            single.add(cur)
            for node in adjlist[cur]:
                if node not in visited:
                    queue.append(node)
                    single.add(node)
                    visited.add(node)
        path.append(set(single))

    queue = deque()
    visited = set()
    queue.append(1)
    level = 0
    while queue:
        n = len(queue)
        while n:
            n -= 1
            cur = queue.popleft()
            if len(adjlist[cur]) == 1 and cur != 1:
                flag = 1
                break
            for node in adjlist[cur]:
                if node not in visited and node not in path[level]:
                    queue.append(node)
                    visited.add(node)

        if flag:
            break
        level += 1
    
    if flag:
        print("YES")
    else:
        print("NO")
    l = [1,2,3]
    print(l[:-1])
            

    
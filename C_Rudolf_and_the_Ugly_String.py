from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    s = list(s)
    x = ["p", "i", "e"]
    x = deque(x)
    y = ["m", "a", "p"]
    y = deque(y)
    mp = {}
    l = 0
    r = 2
    ans = 0
    cur = deque(list(s[l:r+1]))
    while r < n-1:
        if cur == x:
            cur[0] = "z"
            s[l] = "z"
            ans += 1
        elif cur == y:
            cur[-1] = "z"
            s[r] = "z"
            ans += 1
        cur.popleft()
        l +=1
        r += 1
        cur.append(s[r])
    if cur == x:
        cur[0] = "z"
        s[l] = "z"
        ans += 1
    elif cur == y:
        cur[-1] = "z"
        s[r] = "z"
        ans += 1
        
    print(ans)
    
        
        
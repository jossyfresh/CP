t = int(input())
for _ in range(t):
    n = int(input())
    w = list(map(int,input().split()))
    prefix = []
    postfix = {}
    Sum = 0
    for i in range(len(w)):
        Sum += w[i]
        prefix.append(Sum)
    Sum = 0
    for i in range(len(w)-1,-1,-1):
        Sum += w[i]
        postfix[Sum] = i
    ans = []

    for i in range(len(prefix)):
        if prefix[i] in postfix:
            ans.append((i,postfix[prefix[i]]))
    res = 0
    for x in ans:
        if x[0] == n-1 and x[1] == 0 or x[0] == x[1] or x[0] > x[1]:
            continue
        else:
            l = (x[0] - 0)
            r = (n - x[1])
            res = max(res,l + r + 1)
    print(res)
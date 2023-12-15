from collections import Counter
t =  int(input())
for _ in range(t):
    a,b = map(str,input().split())
    B = Counter(b)
    c = 0
    for i in range(len(a)):
        if a[i] in B and B[a[i]] > 0:
            B[a[i]] -= 1
            c += 1
        else:
            break
    print(c)
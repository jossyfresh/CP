t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    l = 0
    r = 2
    c = 0
    while r < len(s):
        if s[r] != s[l]:
            c += 1
        r += 1
        l += 1
    print(c+1)

    
    
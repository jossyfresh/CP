n,t = map(int,input().split())
s = input()
s = list(s)
for j in range(t):
    l = 0
    r = 1
    while r < len(s):
        if s[l] == "B" and s[r] == "G":
            s[l] = "G"
            s[r] = "B"
            l += 2
            r += 2
        else:
            l += 1
            r += 1
print("".join(s))
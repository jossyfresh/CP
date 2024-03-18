t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    c = {"b","c","d"}
    v = {"a","e"}
    s = list(s)
    ans = []
    x = []
    i = 0
    while i < len(s):
        if len(x) == 0:
            x.append(s[i])
            i += 1
        elif len(x) == 1:
            x.append(s[i])
            i += 1
        else:
            if i+1 < len(s) and s[i+1] not in v or i+1 >= len(s):
                x.append(s[i])
                ans.extend(x)
                ans.append(".")
                x = []
                i += 1
            else:
                ans.extend(x)
                ans.append(".")
                x = []
        
    ans.extend(x)
    ans.append(".")
    x = []
    while ans[-1] == ".":
        ans.pop()
    print("".join(ans))
    
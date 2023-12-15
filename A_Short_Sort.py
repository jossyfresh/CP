t = int(input())
strs = "abc"
for _ in range(t):
    a = input()
    c = 0
    for i in range(len(a)):
        if a[i] != strs[i]:
            c += 1
    if c <= 2:
        print("YES")
    else:
        print("NO")
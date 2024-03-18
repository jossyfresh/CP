t= int(input())
for _ in range(t):
    n = int(input())
    if n % 2 != 0:
        print("NO")
    else:
        s = ""
        n = n // 2
        for i in range(n):
            s += "AA"
            s += "Z"
        print("YES")
        print(s)

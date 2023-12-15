t = int(input())
for _ in range(t):
    s = int(input())
    x = []
    Sum = 0
    n = 9
    while True:
        if Sum >= s:
            break
        if Sum + n > s:
            x.append(s-Sum)
            Sum += n
            n -= 1
        else:
            Sum += n
            x.append(n)
            n -= 1
    x.sort()
    ans  = ""
    for y in x:
        ans += str(y)
    print(int(ans))
    

        
    
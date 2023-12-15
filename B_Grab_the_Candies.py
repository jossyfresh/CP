t = int(input())
for a in range(t):
    n = int(input())
    num = list(map(int,input().split()))
    even = 0
    odd = 0
    for x in num:
        if x%2 ==0:
            even+=x
        else:
            odd+=x
    if even > odd:
        print("YES")
    else:
        print("NO")
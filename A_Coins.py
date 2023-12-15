t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    flag = 0
    if n % k == 0 or n%2 == 0:
        flag = 1
    if (n-k) % 2 == 0:
        flag = 1
    if flag:
        print("YES")
    else:
        print("NO")
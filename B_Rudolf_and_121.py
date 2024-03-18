t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    time = 0
    flag = True
    for i in range(len(a)-2):
        time = a[i]
        a[i] -= time
        a[i+1] -= time * 2
        a[i+2] -= time
    for i in range(len(a)):
        if a[i] != 0:
            flag = False
            break
    if flag:
        print('YES')
    else:
        print('NO')


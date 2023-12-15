t = int(input())
for _ in range(t):
    n = int(input())
    m = {}
    count = 0
    num = list(map(int,input().split()))
    for x in num:
        len_ = int.bit_length(x)-1
        m[len_] = m.get(len_,0) + 1
    for x in m:
        count += (m[x] * (m[x]-1))//2
    print(count)
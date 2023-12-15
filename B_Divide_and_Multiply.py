t = int(input())
for _ in range(t):
    n =  int(input())
    num = list(map(int,input().split()))
    count = 0
    for i in range(len(num)):
        while num[i] % 2 == 0:
            num[i] //= 2
            count += 1
    val = 0
    num.sort()
    indx = 0
    flag = 0
    for i in range(len(num)-1,-1,-1):
        if num[i] % 2 != 0 and not flag:
            val += num[i] * 2**count
            flag = 1
        else:
            val += num[i]
    print(val)

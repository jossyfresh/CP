import math
n,p = map(int,input().split())
num = list(map(int,input().split()))
ans = sum(num)
if p > ans:
    ans = math.ceil(p/ans)
res = 0
for i in range(len(num)):
    val = 0
    k = 0
    j = i
    flag = 0
    while k < len(num):
        val += num[j]
        if val >= p:
            if k < ans:
                res = (i+1,k+1)
                ans = k
            flag = 1
            break
        if j == len(num)-1:
            j = -1
        j += 1
        k += 1
    if not flag:
        if p % val == 0:
            if (p//val)*len(num) < ans:
                res = (i+1,(p//val)*len(num))
                ans = (p//val)*len(num)
        else:
            rem = math.ceil(p / val)
            rem = val * rem
            print(rem)
            j = i-1
            l = len(num)
            while rem:
                if rem - num[j] < p:
                    break
                rem -= num[j]
                l -= 1
                if j == 0:
                    j = len(num)
                j -= 1
            if (p//val)*l < ans:
                res = (i+1,(p//val)*len(num) + l)
                ans = (p//val)*len(num) + l
print(*res)


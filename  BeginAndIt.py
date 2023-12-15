import itertools
n = int(input())
num = list(map(int,input().split()))
nums = []
min_ = min(num)
for i in range(len(num)):
    num[i] += abs(min_)
new = [list(group) for k,group in itertools.groupby(num, lambda x: x==0) if not k]
cur = 0
val = 0
ans = 0
print(new)
for j in range(len(new)):
    x = new[j]
    flag = 0
    for i in range(len(x)):
        if cur <= x[i] and not flag:
            cur = x[i]
        elif cur > x[i] and not flag:
            val = x[i]
            flag = 1
        elif cur >= x[i] and flag:
            if val > x[i]:
                val = x[i]
        elif cur < x[i] and flag:
            flag = 0
            ans += cur
        else:
            continue
        
        


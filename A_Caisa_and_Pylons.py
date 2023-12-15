n =  int(input())
num = list(map(int,input().split()))
num.insert(0,0)
ans = []
for i in range(len(num)-1):
    val = num[i] - num[i+1]
    ans.append(val)
Sum = 0
for i in range(len(ans)):
    Sum += ans[i]
    ans[i] = Sum
min_= min(ans)
if min_ < 0:
    print(abs(min_))
else:
    print(0)

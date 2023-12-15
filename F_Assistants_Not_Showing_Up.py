n,m = map(int,input().split())
num = [0] * (n)
for i in range(m):
    x,y = map(int,input().split())
    num[x] += 1
    if y < n-1:
        num[y+1] -= 1
Sum = 0 
for x in range(len(num)): 
    Sum += num[x]
    num[x] = Sum
flag = 1
for j in range(0,n):
    x = num[j]
    if x == 0:
        print("YES")
        flag = 0
        break
if flag:
    print("NO")
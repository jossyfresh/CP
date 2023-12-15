n = int(input())
num = list(map(int,input().split()))
edge = []
for i in range(n):
    edge.append((i+1,num[i]))
flag = 0
c = set(edge)
for u, v in edge:
  for w in num:
     if (v, w) in c and (w, u) in c and w != u and w != v:
          flag = 1
if flag:
    print("YES")
else:
    print("NO")

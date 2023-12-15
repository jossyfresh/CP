import math
t = int(input())
for _ in range(t):
    a,b,c = map(int,input().split())
    val = math.ceil((max(b,a)-min(a,b)) / (2*c))
    print(val)
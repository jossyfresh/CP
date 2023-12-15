n = int(input())
x = input()
y = input()
rep = {chr(i):chr(i) for i in range(97,97+26)}
def find(x):
    if rep[x] != x:
        rep[x] = find(rep[x])
    return rep[x]
def union(x,y):
    repx = find(x)
    repy = find(y)
    if repx == repy:
        return 
    if ord(repx) < ord(repy):
        rep[repy] = repx
    else:
        rep[repx] = repy
for i in range(n):
    union(x[i],y[i])
ans = []
for i in range(97,97+26):
    a = find(chr(i))
    if a != chr(i):
        ans.append((chr(i),a))
print(len(ans))
for x in ans:
    print(f'{x[0]} {x[1]}')
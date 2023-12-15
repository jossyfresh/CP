n = int(input())
p = list(map(int,input().split()))
l = list(map(int,input().split()))
x = p[1:]
y = l[1:]
x = set(x)
final = x.union(set(y))
if len(final) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
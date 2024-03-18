def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    num = (a * b) // gcd(a, b)
    if num == b:
        print(num * (b//a))
    else:
        print(num)
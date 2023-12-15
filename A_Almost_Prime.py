n = int(input())
count = 0
for i in range(1,n+1):
    a = set()
    d = 2
    while d * d <= i:
        while i % d == 0:
            a.add(d)
            i //= d
        d+=1
    if i > 1:
        a.add(i)
    if len(a) == 2:
        count +=1 
print(count)
from collections import Counter
t = int(input())
for _ in range(t):
    s = input()
    n = Counter(s)
    new = sorted(n.items(),key = lambda x:x[1])
    new.reverse()
    for x in new:
        if x[1]==3:
            print(6)
        elif x[1] == 4:
            print(-1)
        else:
            print(4)
        break

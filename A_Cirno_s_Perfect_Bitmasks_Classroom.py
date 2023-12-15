t = int(input())
for _ in range(t):
    x = int(input())
    if x % 2 != 0:
        if x == 1:
            print(3)
        else:
            print(1)
    else:
        if 2 ** 30 % x == 0:
            print(x + 1)
        else:
            print(x & -x)
    
    
t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    high,low = 0,0
    if a >= b:
        high = a
        low = b
    else:
        high = b
        low = a
    if low == 1:
        res = 0
        res += 1
        res += high // 2
        res += low
    elif low % 2 != 0 and high %2 != 0 and high % low != 0:
        res = high + low 
    else:
        res = 0
        val = high % low
        ju = high // low
        res += val
        res += ju
        res += low
    print(res)


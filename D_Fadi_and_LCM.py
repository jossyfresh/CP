import math
x = int(input())
def factor(x,factors):
    for i in range(1,int(math.sqrt(x)) +1):
        if x % i == 0:
            factors.append(i)
            if i != x // i:
                factors.append(x//i)
    return factors
if x == 1:
    val = [1,1]
else:
    num = factor(x,[])
    min_ = x
    val = []
    for y in num:
        if max((y,x // y)) <= x:
            if y != x//y:
                val = (y,x //y)
                min_ = max(y,x//y)
print(*val)

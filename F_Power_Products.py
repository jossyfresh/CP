n,k = map(int,input().split())
import math
num = list(map(int,input().split()))
def pfactor(n):
    i = 2
    prime_factors = []
    while i*i <= n:
        if n%i == 0:
            if len(prime_factors) > 0 and prime_factors[-1][0] == i:
                prime_factors[-1][1] += 1
            elif len(prime_factors) == 0 or prime_factors[-1][0] != i:
                prime_factors.append([i,1]) 
            n //= i
        else:
            i += 1
    if n>1:
        if len(prime_factors) > 0 and prime_factors[-1][0] == n:
                prime_factors[-1][1] += 1
        elif len(prime_factors) == 0 or prime_factors[-1][0] != n:
            prime_factors.append([n,1]) 
    return prime_factors
m = {}
count = 0
for x in num:
    pf = pfactor(x)
    val = []
    needed = []
    for y in pf:
        if y[1] % k != 0:
            needed.append((y[0],abs(y[1]-k)])
        val.append((y[0],(y[1] % k)))
    if not needed:
        needed = [(1,1)]
    val = tuple(val)
    needed = tuple(needed)
    if val in m:
        count += m[val]
    m[needed] = m.get(needed,0) + 1
    print(m)
   
    


      
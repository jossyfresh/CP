n,k = map(int,input().split())
prev = n
arr = []
x = bin(n)
x = x[2:]
l = len(x)
j = 0
while n:
    nu = n & 1
    arr.append(nu * 2 ** j)
    j += 1
    n = n>>1
print(arr)
new = []
for i in range(len(arr)-1,-1,-1):
    if arr[i] > 2:
        x = [2] * (arr[i] // 2)
        new.extend(x)
    elif arr[i] != 0:
        new.append(arr[i])
new = new[::-1]
r = len(new)-1
while len(new) > k:
    val = new.pop()
    new[r-1] += val
    r -= 1
if len(new) !=  k:
    print("NO")
elif len(new) == k:
    flag = 1
    Sum = 0
    for i in range(len(new)):
        Sum += new[i]
        if 2 ** 30 % new[i] != 0:
            flag = 0
            break
    if Sum != prev:
        flag = 0
    if flag:
        print("YES")
        print(*new)
    else:
        print("NO")




















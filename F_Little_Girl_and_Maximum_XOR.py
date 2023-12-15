l,r = map(int,input().split())

val = l ^ r
count = 0
while val:
    val = val>>1
    count += 1
temp = 1
while count:
    temp <<= 1
    count -= 1
print(temp-1)



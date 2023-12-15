x = int(input())
i = 1
count = 1
while x//2 > 0:
    if x % 2 != 0:
        count += 1
    x = x // 2
print(count)
import itertools
n = int(input())
count = 0
curr = 0
while True:
    sum = 0
    x = curr
    while(x):
        sum = sum + x % 10
        x = x // 10
    if (sum == 10):
        count = count + 1
    if (count == n):
        print(curr)
        exit()
    curr += 1

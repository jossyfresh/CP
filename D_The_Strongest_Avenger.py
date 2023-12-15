t = int(input())
for _ in range(t):
    n = int(input())
    arr = input()
    arr = list(arr)
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    maps = {}
    maps[0] = 1
    Sum = 0
    count = 0
    for i in range(len(arr)):
        Sum += arr[i]
        if Sum-i-1 not in maps:
            maps[Sum-i-1] = 0
        count += maps[Sum-i-1]
        maps[Sum-i-1] += 1
        
    print(count)



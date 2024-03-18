t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    ans = [arr[0]]
    odd = 0
    even = 0
    if arr[0] % 2 == 0:
        even += 1
    else:
        odd += 1
    s = arr[0]
    for i in range(1,len(arr)):
        if arr[i] % 2 == 0:
            even += 1
        else:
            odd += 1
        s += arr[i]
        if odd == 2 or odd == 0:
            ans.append(s)
        elif odd % 2 != 0:
            ans.append(s-(((odd%3)%2) + odd // 3))
        elif odd % 2 == 0:
            ans.append(s-(((odd%3)%2) + odd // 3))
    print(*ans)        
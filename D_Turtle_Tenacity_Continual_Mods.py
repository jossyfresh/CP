from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    # c = Counter(arr)
    arr.sort()
    if arr[0] != arr[1]:
       print("YES")
    else:
        for num in arr:
            if num % arr[0] != 0:
                print("YES")
                break
        else:
            print("NO")     
    
        
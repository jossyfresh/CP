T = int(input())
for _ in range(T):
    n = int(input())
    if n < 6:
        print("NO")
    else:
        if n % 3 == 0:
            if n - 5 != 1 and n-5 != 4:
                ans = [1,4,n-5]
                print("YES")
                print(*ans)
            else:
                print("NO")
        else:
            if n-3 != 1 and n-3 != 3:
                ans = [1,2,n-3]
                print("YES")
                print(*ans)
            else:
                print("NO")
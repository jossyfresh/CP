n = int(input())

ans = float("inf")
for i in range(1,6):
    if n % i == 0:
        if n // i < ans:
            ans = (n // i)
    else:
        if n // i < ans:
            ans = ((n // i)+1)
            
print(ans)
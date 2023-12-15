n = int(input())
ans = ""
for i in range(n):
    if i % 2 == 0:
        ans += "I hate"
        if i < n-1:
            ans += " that "
    else:
        ans += "I love"
        if i < n-1:
            ans += " that "
ans += " it"
print(ans)
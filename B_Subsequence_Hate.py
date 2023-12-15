t = int(input())
for _ in range(t):
    s = input()
    s = list(s)
    for i in range(len(s)):
        if s[i] == "1":
            s[i] = "a"
        else:
            s[i] = "b"
    b_total = s.count('a')
    a_sum = b_sum = 0
    ans = b_total
    for ch in s:
        a_sum += (ch == 'b')
        b_sum += (ch == 'a')
        ans = min(ans, a_sum + (b_total - b_sum))

    b_total = s.count('b')
    a_sum = b_sum = 0
    for ch in s:
        a_sum += (ch == 'a')
        b_sum += (ch == 'b')
        ans = min(ans, a_sum + (b_total - b_sum))
    print(ans)
    
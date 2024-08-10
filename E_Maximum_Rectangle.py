t = int(input())
for _ in range(t):
    s = input()
    max_ = 0
    count = 0
    if '0' not in s:
        print(len(s) ** 2)
        continue
    for i in range(len(s)*2):
        i = i % len(s)
        if s[i] == '1':
            count += 1
            max_ = max(max_,count)
        else:
            count = 0
    width = 1
    ans = 0
    for length in range(max_,0,-1):
        area = width * length
        width += 1
        ans = max(ans,area)
    print(ans)



    



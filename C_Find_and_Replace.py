t = int(input())
for k in range(t):
    n = int(input())
    s = input()
    flag = 0
    for i in range(len(s)):
        x = s[i]
        for j in range(i+1,len(s)):
            val = j+1 - i
            if s[j] == x and val%2==0:
                flag = 1
                break 
    if flag:
        print("NO")
    else:
        print("YES")
s = input()
t = input()
l = 0
r = 0
let = []
flag = 0
while l < len(s) and r < len(t):
    if s[l] != t[r] and flag:
        print(0)
        exit()
    elif s[l] != t[r]:
        let.append(l+1)
        flag = 1
        l += 1
    else:
        l += 1
        r += 1
if l < len(s):
    let.append(l+1)
i = let[0]-2
j = let[0]
ans = []
ans.append(let[0])
while i >= 0:
    if s[i] == s[let[0]-1]:
        ans.append(i+1)
    else:
        break
    i -= 1
while j < len(s):
    if s[j] == s[let[0]-1]:
        ans.append(j+1)
    else:
        break
    j += 1
ans.sort()
print(len(ans))
print(*ans)

s = input()
t = input()
j = len(t)-1
i = len(s)-1

let = 0
while i >= 0 and j >= 0:
    if s[i] == t[j]:
        let += 1
    else:
        break
    j -= 1
    i -= 1
print(len(s)+len(t)-(let*2))

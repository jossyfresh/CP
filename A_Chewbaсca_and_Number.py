n = int(input())
s = str(n)
s = list(s)
for i in range(len(s)):
    if i == 0:
        if int(s[i]) >= 5 and int(s[i])!=9:
            s[i] = str(9 - int(s[i]))
    else:
        if int(s[i]) >= 5:
            s[i] = str(9 - int(s[i]))
x = "".join(s)
print(int(x))
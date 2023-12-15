a = input().split("+")
for i in range(len(a)):
    a[i] = int(a[i])
a.sort()
s = ""
for i in range(len(a)-1):
    s += f'{a[i]}+'
s += str(a[-1])
print(s)
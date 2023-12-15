n = int(input())
n = str(n)
flag = 0
for x in n:
    if int(x) == 4 or int(x) == 7:
        flag += 1
if flag == 4 or flag == 7:
    print("YES")
else:
    print("NO")

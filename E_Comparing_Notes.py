x =  input()
y = input()
i = 0
j = 0
flag = 0
i = 0
j = 0 
while i < len(x) and j < len(y):
    if x[i] == "-" or y[j] == "-":
        break
    if x[i] != y[j]:
        flag = 1
    i += 1
    j += 1
i =  len(x)-1
j = len(y)-1
while i >= 0 and j >=0 :
    if x[i] == "-" or y[j] == "-":
        break
    if x[i] != y[j]:
        flag = 1
    i -= 1
    j -= 1
if flag:
    print("NO")
else:
    print("YES")

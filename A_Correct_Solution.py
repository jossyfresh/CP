n = input()
res = input()
check = []
for i in range(len(res)):
    check.append(int(res[i]))
if "0" in n:
    num = []
    for i in range(len(n)):
        num.append(int(n[i]))
    num.sort()
    ans = []
    j = 0
    for i in range(len(num)):
        if j== 0 and num[i] != 0:
            ans.insert(0,num[i])
            j = 1
        else:
            ans.append(num[i])
else:
    num = []
    for i in range(len(n)):
        num.append(int(n[i]))
    num.sort()
    ans = []
    for i in range(len(num)):
        ans.append(num[i])
flag = 0
if len(check) == len(ans):
    for i in range(len(ans)):
        if check[i] != ans[i]:
            flag = 1
else:
    flag = 1
if not flag:
    print("OK")
else:
    print("WRONG_ANSWER")
    
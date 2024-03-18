t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    i = 0
    j = len(a)-1
    flag = True
    while i < j:
        if a[i] == a[j]:
            i += 1
            j -= 1
        else:
            if ord(a[i]) > ord(a[j]):
                flag = False
                break
            else:
                flag = True
                break
    if flag:
        print(a)
    else:
        y = a
        x = a[::-1]
        print(x+y)
                
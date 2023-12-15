t = int(input())
for _ in range(t):
    s = input()
    s = list(s)
    c = 0
    flag = 0
    p = "05"
    y =  ["05","27"]
    i = len(s)-1
    while i >= 0 and s[i] != "0":
        i -= 1
        c += 1
    j = i - 1
    while j >=0 and s[j] not in y[0]:
        j -= 1
        c += 1 
    a = 0
    l = len(s)-1
    while l >= 0 and s[l] != "5":
        l -= 1
        a += 1
    k = l -1
    while k >= 0 and s[k] not in y[1]:
        k -= 1
        a += 1
    print(min(a,c))


        

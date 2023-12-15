s = input()
ans = []
l = False
flag = 0
for i in range(len(s)-1):
    if not l:
        if s[i] == "A" and s[i+1] == "B":
                ans.append((i,i+1))
                l = True
    else:
        if s[i] == "B" and s[i+1] == "A":
            if ans and ans[-1][1] != i:
                ans.append((i,i+1))
                flag = 1
                break
l = False
ans = []
for i in range(len(s)-1):
    if not l:
        if s[i] == "B" and s[i+1] == "A":
            ans.append((i,i+1))
            l = True
    else:
        if s[i] == "A" and s[i+1] == "B":
            if ans and ans[-1][1] != i:
                ans.append((i,i+1))
                flag = 1
                break  
if flag:
    print("YES")
else:
    print("NO")
                


    

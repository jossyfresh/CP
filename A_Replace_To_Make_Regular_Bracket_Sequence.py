s = input()
stack = []
opening = "[{<("
closing = "]>})"
flag = 0
stack2 = []
for x in s:
    if stack2 and stack2[-1] in opening:
        if x == ")" and stack2[-1] == "(":
            stack2.pop()
        elif x == "}" and stack2[-1] == "{":
            stack2.pop()
        elif x == "]" and stack2[-1] == "[":
            stack2.pop()
        elif x == ">" and stack2[-1] == "<":
            stack2.pop()
        else:
            stack2.append(x)
    else:
        stack2.append(x)
n = len(stack2)
c = 0
ans = 0
for x in stack2:
    if x in closing and stack and stack[-1] in opening:
        if x == ")" and stack[-1] == "(":
            c += 1
        elif x == "}" and stack[-1] == "{":
            c += 1
        elif x == "]" and stack[-1] == "[":
            c += 1
        elif x == ">" and stack[-1] == "<":
            c += 1
        else:
            ans += 1
        stack.pop()
    else:
        stack.append(x)
if stack:
    flag = 1
if flag:
    if s == "":
        print(0)
    else:
        print("Impossible")
    
else:
    print(ans)


    
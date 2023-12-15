n,k = map(int,input().split())
n = str(n)

n = list(n)
stack  = [int(x) for x in n]

while k:
    if stack[-1] == 0:
        stack.pop()
        
    else:
        stack[-1] -= 1
    k -= 1
ans = [str(x) for x in stack]
print("".join(ans))


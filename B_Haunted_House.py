for i in range(int(input())):
    n=int(input())
    s=input()
    stack=[]
        
    for i,j in enumerate(s[::-1]):
 
        if j=='0':
            stack.append(i-len(stack))
    ans=[]
    cur=0
    for i in range(len(stack)):
        cur+=stack[i]
        ans.append(cur)
    ans+=[-1]*(n-len(ans))
    print(*ans)
            

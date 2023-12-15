from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    sets = []
    count = defaultdict(int)
    for i in range(n):
        x = list(map(int,input().split()))
        sets.append(set(x[1:]))
    total = set()
    for x in sets:
        total.update(x)
        for j in x:
            count[j] += 1
    ans = 0
    for i in range(50+1):
        new = set()
        for j in sets:
            if i not in j:
                new.update(j)
        if len(new) != len(total):
            ans = max(ans,len(new))
    print(ans)
        

   
              

        
        
    
            
    
    
n = int(input())
ins = set()
ans = 0 
num = []
for _ in range(n):
    x = input()
    if x[0] == "+":
        num.append(x)     
    else:
        num.append(x)
count = 0
c = 0
for i in range(len(num)):
    
ans = max(ans,len(ins))
print(ans)

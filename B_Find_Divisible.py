t=  int(input())
for _ in range(t):
    l,r = map(int,input().split())
    if l == 1:
        print(f'{l} {r}')
    else:
        print(f'{l} {l*2}')

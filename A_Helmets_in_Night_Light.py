t= int(input())
for _ in range(t):
    n,p = map(int,input().split())
    person = list(map(int,input().split()))
    cost = list(map(int,input().split()))
    person.append(n)
    cost.append(p)
    people = list(zip(cost,person))
    people.sort()
    ans = p
    totalp = n-1
    for x,y in people:
        if totalp <= 0:
            break
        ans += x*min(totalp,y)
        totalp -= y
    print(ans)




n = int(input())
women = []
rat = []
cap = []
man = []
for _ in range(n):
    name,xcs = input().split()
    if xcs == "rat":
        rat.append((name,_))
    elif xcs == "woman" or xcs == "child":
        women.append((name,_))
    elif xcs == "man":
        man.append((name,_))
    else:
        cap.append((name,_))
rat.sort(key=lambda x: x[1])
women.sort(key=lambda x: x[1])
man.sort(key=lambda x: x[1])
cap.sort(key=lambda x: x[1])
for i in rat:
    print(i[0])
for i in women:
    print(i[0])
for i in man:
    print(i[0])
for i in cap:
    print(i[0])
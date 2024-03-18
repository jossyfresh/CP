t = int(input())
for _ in range(t):
    x = input()
    y = input()
    z = input()
    let = set()
    if "?" in x:
        for i in range(len(x)):
            let.add(x[i])
    elif "?" in y:
        for i in range(len(y)):
            let.add(y[i])
    else:
        for i in range(len(z)):
            let.add(z[i])
    if "A" not in let:
        print("A")
    elif "B" not in let:
        print("B")
    else:
        print("C")
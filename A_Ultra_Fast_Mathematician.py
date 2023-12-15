n1 = input()
n2 = input()
max_ = max(len(n1),len(n2))
value1 = int(n1, 2)
value2 = int(n2,2)
x = (value1 ^ value2)
y = format(x, "b")
if len(y) < max_:
    ans = "0" * (max_ - len(y))
    print(ans + y)
else:
    print(y)

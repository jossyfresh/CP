n = int(input())
val = 0
for _ in range(n):
    s = input()
    if s == "++X" or s == "X++":
        val += 1
    else:
        val -= 1
print(val)
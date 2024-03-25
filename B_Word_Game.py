t = int(input())
for _ in range(t):
    n = int(input())
    words = []
    dict = {}
    for _ in range(3):
        word = list(map(str, input().split()))
        for x in word:
            dict[x] = dict.get(x, 0) + 1
        words.append(word)
    for i in range(3):
        total = 0
        for word in words[i]:
            if dict[word] == 1:
                total += 3
            elif dict[word] == 2:
                total += 1
        # print each guys total
        print(total, end=" ")
    # print a new line
    print()
    
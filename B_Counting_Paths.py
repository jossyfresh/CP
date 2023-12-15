MOD = 10**9 + 7

for _ in range(int(input())):
  a, b = map(int, input().split())

  if b == 0:
    print(1)
  elif a == b:
    print(2)
  else:
    ways = [[0] * (b+1) for _ in range(a+1)]
    ways[0][0] = 1

    for i in range(1, a+1):
      for j in range(0, min(i, b)+1):
        if j > 0:
          ways[i][j] += ways[i-1][j-1] 
        if j < i:
          ways[i][j] += ways[i-1][j]
        ways[i][j] %= MOD

    print(ways[a][b])
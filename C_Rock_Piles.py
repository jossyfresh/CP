for _ in range(int(input())):
  n, m = map(int, input().split())
  
  if n % 2 == 0 and m % 2 == 0:
    print("abdullah")
  elif n % 2 == 1 and m % 2 == 1: 
    print("hasan")
  elif n == 0:
    print("abdullah")
  elif m == 0:
    print("hasan")
  elif n % 2 == 0:
    print("hasan")
  else:
    print("abdullah")
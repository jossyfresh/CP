import sys,threading
from collections import defaultdict,deque
from decimal import Decimal
def main():
    n = int(input())
    # chatGpt gave me the Decimal import
    a = list(map(Decimal, input().split()))
    b = list(map(Decimal, input().split()))
    mp = {}
    rest = 0
    for i in range(n):
        if a[i] == 0 and b[i] == 0:
            rest += 1
        elif a[i] == 0:
            continue
        else:
            x = b[i] / a[i]
            mp[x] = mp.get(x, 0) + 1
    ans = 0
    if len(mp) == 0:
        print(rest)
        return
    print(max(list(mp.values()))+rest)
    return

sys.setrecursionlimit(1 << 30)

threading.stack_size(1 << 27)

main_thread = threading.Thread(target = main)

main_thread.start()

main_thread.join()
    

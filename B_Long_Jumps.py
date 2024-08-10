import sys,threading
from collections import defaultdict

def main():
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        arr = list(map(int, input().split()))
        memo = {}
        def dp(i):
            if i in memo:
                return memo[i]
            if i >= n:
                return 0
            memo[i] = arr[i] + dp(i+arr[i])
            return arr[i] + dp(i+arr[i])
        ans = 0
        for i in range(n):
            ans = max(ans, dp(i))
        print(ans)
        
sys.setrecursionlimit(1 << 30)

threading.stack_size(1 << 27)

main_thread = threading.Thread(target = main)

main_thread.start()
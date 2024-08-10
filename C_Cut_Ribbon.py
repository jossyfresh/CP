import sys,threading
from collections import defaultdict

def main():
    n,a,b,c = map(int,input().split())
    min_ = min(a,b,c)
    ans = [0]
    memo = {}
    def dp(i,len,arr):
        if i in memo:
            return memo[i]
        if i >= n:
            if i == n:
                ans[0] = max(ans[0],len)
                return 0
            return -10000000
        memo[i] = max(1 + dp(i+a,len+1,arr + [a]) , 1 + dp(i+b,len+1,arr + [b]) , 1+ dp(i+c,len+1,arr + [c]))
        return max(1 + dp(i+a,len+1,arr + [a]) , 1 + dp(i+b,len+1,arr + [b]) , 1 + dp(i+c,len+1,arr + [c]))
    print(dp(0,0,[]))
        
sys.setrecursionlimit(1 << 30)

threading.stack_size(1 << 27)

main_thread = threading.Thread(target = main)

main_thread.start()
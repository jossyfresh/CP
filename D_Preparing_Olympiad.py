import sys,threading
from collections import defaultdict,deque
def main():
    n,l,r,x = map(int,input().split())
    num = list(map(int,input().split()))
    def dp(i,count,mi,ma):
        if i == len(num):
            if count <= r and count >= l and abs(mi - ma) >= x:
                return 1
            return 0
        return dp(i+1,count +num[i],min(mi,num[i]),max(ma,num[i])) + dp(i+1,count,mi,ma)
    print(dp(0,0,float("inf"),0))

sys.setrecursionlimit(1 << 30)

threading.stack_size(1 << 27)

main_thread = threading.Thread(target = main)

main_thread.start()

main_thread.join()
    

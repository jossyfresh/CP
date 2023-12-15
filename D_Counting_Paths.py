import sys,threading
from collections import defaultdict
def main():
    T = int(input())
    for _ in range(T):
        a, b = map(int, input().split())
    
        mem = defaultdict(int)
        def countPath(length, prev, change):
            if length == a:
                if change == b:
                    return 1
                else:
                    return 0
            
            if (length, prev, change) in mem:
                return mem[(length, prev, change)]
                
            l, r = change, change
            if prev != 1 and prev != 0:
                l += 1
            if prev != -1 and prev != 0:
                r += 1
    
            left = countPath(length + 1, 1, l)
            right = countPath(length + 1, -1, r)
            mem[(length, prev, change)] = left + right 
            return mem[(length, prev, change)]
    
    
        result = countPath(0, 0, 0)
        print(result)
sys.setrecursionlimit(1 << 30)

threading.stack_size(1 << 27)

main_thread = threading.Thread(target = main)

main_thread.start()

main_thread.join()
    

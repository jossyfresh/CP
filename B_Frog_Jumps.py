import sys,threading
def main():
    t = int(input())
    for _ in range(t):
        s = str(input())
        ans = 0
        c = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == "R":
                ans = max(ans,c)
                c = 0
            else:
                c += 1
        ans = max(ans,c)
        print(ans+1)
        
sys.setrecursionlimit(1 << 30)

threading.stack_size(1 << 27)

main_thread = threading.Thread(target = main)

main_thread.start()

main_thread.join()
    

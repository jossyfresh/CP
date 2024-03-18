import sys,threading
from collections import deque
def main():
    t = int(input())
    for _ in range(t):
        n,m,x = map(int, input().split())
        cur = set()
        cur.add(x)
        for _ in range(m):
            r,c = map(str, input().split())
            r = int(r)
            size = len(cur)
            people = list(cur)
            cur = set()
            for i in range(size):
                node = people.pop()
                if c == "?":
                    nextval1 = ((n + node - r) % n)
                    if nextval1 == 0:
                        nextval1 = n
                    nextval2 = (((node + r) - 1) % n) + 1
                    if nextval2 == 0:
                        nextval2 = n
                    cur.add(nextval1)
                    cur.add(nextval2) 
                elif c == "1":
                    nextval = ((n + node) - r) % n
                    if nextval == 0:
                        nextval = n
                    cur.add(nextval) 
                else:
                    nextval = ((node + r) - 1) % n + 1
                    if nextval == 0:
                        nextval = n
                    cur.add(nextval)
        cur = list(cur)
        cur.sort()
        print(len(cur))
        print(*cur)
 
sys.setrecursionlimit(1 << 30)
 
threading.stack_size(1 << 27)
 
main_thread = threading.Thread(target = main)
 
main_thread.start()
 
main_thread.join()
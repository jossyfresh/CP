import sys,threading
from collections import defaultdict
def main():
    t =int(input())
    for _ in range(t):
        adjlist = defaultdict(list)
        n = int(input())
        nums = list(map(int,input().split()))
        for i in range(len(nums)):
            adjlist[nums[i]].append(i+2)
        s = input()
        ans = [0]
        def dfs(cur):
            if cur not in adjlist:
                if s[cur-1] == "B":
                    return 1 
                else:
                    return -1
            curs = 0
            for node in adjlist[cur]:
                curs += dfs(node)
            if s[cur-1] == "B":
                curs += 1
            elif s[cur-1] == "W":
                curs -= 1
            if not curs:
                ans[0] += 1
            return curs
        if s[0] == "B":
            start = 1
        else:
            start = -1
        dfs(1)
        print(ans[0])

sys.setrecursionlimit(1 << 30)

threading.stack_size(1 << 27)

main_thread = threading.Thread(target = main)

main_thread.start()

main_thread.join()
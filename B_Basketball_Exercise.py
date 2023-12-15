import sys,threading
def main():
    n = int(input())
    num1 = list(map(int,input().split()))
    num2 = list(map(int,input().split()))

    memo = {}
    def dp(i,turn):
        if i == n:
            return 0
        if (i,turn) in memo:
            return memo[(i,turn)]
        if turn == "n":
            memo[(i,turn)] = max(dp(i+1,"n2") + num1[i],dp(i+1,"n1")+num2[i],dp(i+1,"n"))
            return memo[(i,turn)]
        if turn == "n1":
            memo[(i,turn)] = max(dp(i+1,"n2") + num1[i],dp(i+1,"n"))
            return memo[(i,turn)]
        else:
            memo[(i,turn)] =  max(dp(i+1,"n1") + num2[i],dp(i+1,"n"))
            return memo[(i,turn)]
    print(dp(0,"n"))

sys.setrecursionlimit(1 << 30)

threading.stack_size(1 << 27)

main_thread = threading.Thread(target = main)

main_thread.start()

main_thread.join()
    

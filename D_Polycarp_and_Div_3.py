import sys,threading
def main1():
    n =  input()
    num = [int(x) for x in n]
    ans = [0]
    memo = {}
    def dp(i,j,c):
        if i == len(num)+1:
            ans[0] = max(ans[0],c)
            return
        if (i,j) in memo:
            return
        n = str(num[j:i])
        n = n[1:-1]
        string_value = n
        string_value_without_comma = string_value.replace(', ', '')
        integer_value = int(string_value_without_comma)
        if integer_value % 3 == 0:
            c += 1
        dp(i+1,i,c)
        dp(i+1,j,c)
        memo[(i,j)] = c
        return
    dp(1,0,0)
    print(ans[0])
def main():
    s = input()
    n = len(s)
    r = 0
    fin = [-1, -1, -1]
    fin[0] = 0
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        r = (r + int(s[i - 1])) % 3
        dp[i] = dp[i - 1]
        if fin[r] != -1:
            dp[i] = max(dp[i], dp[fin[r]] + 1)
        fin[r] = i
    print(dp[n])
    
sys.setrecursionlimit(1 << 30)

threading.stack_size(1 << 27)

main_thread = threading.Thread(target = main1)

main_thread.start()

main_thread.join()
    

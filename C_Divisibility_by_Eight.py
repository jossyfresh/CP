def main():
    n = input()
    n = list(n)
    ans = [""]
    memo = {}
    flag = 0
    if "0" in n:
        flag = 1
    even = "02468"
    flag2 = 0
    lasteven = 0
    for i in range(len(n)):
        if n[i] in even:
            flag2 = 1
            lasteven = i
    if not flag2:
        print("NO")
        exit()
    def dp(i,number):
        if (i,number) in memo:
            return 
        if i == len(n):
            if number % 8 == 0:
                if number == 0 and flag:
                    ans[0] = number
                    return 
                if number > 0:
                    ans[0] = number
                    return
            return 
        if lasteven+1 == i:
            if number % 8 == 0:
                if number == 0 and flag:
                    ans[0] = number
                    return 
                if number > 0:
                    ans[0] = number
                    return
            return
        if number % 8 == 0:
            if number == 0 and flag:
                ans[0] = number
                return 
            if number > 0:
                ans[0] = number
                return
        dp(i+1,(number*10)+int(n[i]))
        dp(i+1,number)
        memo[(i,number)] = 1
        return 
    dp(0,0)
    if ans[0] != "":
        print("YES")
        print(ans[0])
    else:
        print("NO")
main()
t = int(input())
for _ in range(t):
    x,k = map(int,input().split())
    MAXN = 10**10
    def sumOfDigits(n): 
        sum = 0
        while(n > 0):
            sum += n % 10

            n //= 10
        return sum
    def smallestNum(X, Y):
        res = -1; 
        for i in range(X, MAXN):
            sum_of_digit = sumOfDigits(i)

            if sum_of_digit % Y == 0:
                res = i
                break
        
        return res  
    print(smallestNum(x,k))   


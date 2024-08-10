n = int(input())
arr = list(map(int,input().split()))
l = 0 
r = n - 1
alice = 0
bob = 0
l = 0
r = n - 1
while l <= r:
    if alice <= bob:
        alice += arr[l]
        l += 1
    else:
        bob += arr[r]
        r -= 1
print(l,n - r - 1)

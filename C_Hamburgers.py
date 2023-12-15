S = input()
b,s,c = map(int,input().split())
b1,s1,c1 = map(int,input().split())
m = int(input())
b2 = 0
s2 = 0
c2 = 0
for x in S:
    if x == "B":
        b2+=1
    elif x == "C":
        c2+=1
    else:
        s2+=1
b3 = 0 if b2 == 0 else b//b2
c3 = 0 if c2 ==0 else c//c2
s3 = 0 if s2 == 0 else s//s2
val = min(b3,c3,s3)
print(val)
    

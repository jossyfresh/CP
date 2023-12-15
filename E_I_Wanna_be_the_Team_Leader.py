import heapq,bisect
n,m = map(int,input().split())
ni = [1,2,3]
print(bisect.bisect_left(ni,1))
programmer = list(map(int,input().split()))
for i in range(len(programmer)):
    programmer[i] = (programmer[i],i)
programmer.sort()
project = list(map(int,input().split()))
for i in range(len(project)):
    project[i] = (project[i],i)
project.sort()
l = 0
r = 0
ans = []
temp = []
while l < len(project) and r < len(programmer):
    heapq.heappush(temp,(programmer[r][0],programmer[r][1]))
    if (project[l][0]/len(temp)) <= temp[0][0]:
        ans.append(list(temp))
        temp = []
        l += 1
    r += 1
total = 0
# if len(ans) != len(project):
#     print("NO")
# else:
#     print("YES")
#     for x in ans:
#         len_ = len(x)
#         arr = [len_]
#         for val,ind in x:
#             arr.append(ind+1)
#         print(*arr)
pattern = "aaacaaaa"
print(pattern)
lps_table = [0] * len(pattern)
j = 0
i = 1
while i < len(pattern):
    if pattern[i] == pattern[j]:
        lps_table[i] = j + 1
        i += 1
        j += 1
    else:
        if j > 0:
            j = lps_table[j - 1]
        else:
            lps_table[i] = 0
            i += 1
    print(lps_table,j,i)
print(lps_table)





n,t = map(int,input().split())
nodes = list(map(int,input().split()))
flag = [0]
stack = [0]
while stack:
    cur_node = stack.pop()
    if cur_node == t-1:
        flag[0] = 1
        break
    if cur_node < t:
        stack.append(cur_node+nodes[cur_node])
if flag[0]:
    print("YES")
else:
    print("NO")



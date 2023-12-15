"""Question1
    You have a graph of n nodes labeled from 0 to n - 1. 
    You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.
    Return true if the edges of the given graph make up a valid tree, and false otherwise.
Example                       |
    Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
    Output: true

1 <= n <= 2000
0 <= edges.length <= 5000
edges[i].length == 2
0 <= ai, bi < n
ai != bi
There are no self-loops or repeated edges.

"""
# build the graph 
# i will call another function called validTree and this will return wther the passed graph is valid or not
from collections import defaultdict
from collections import deque

# check if the passed graph is a valid tree. return -> bool
def validTree(graph,n,start):
    visited = set()
    queue = deque()
    queue.append(start)
 
    while queue: # O(n)
        node = queue.popleft()
        if node in visited: return False
        visited.add(node)
        for child in graph[node]:
            queue.append(child)
    if len(visited) == n:
        return True
    return False
def main(n,edges):  
    graph1 = defaultdict(list)
    graph2 = defaultdict(list)
    
    for a,b in edges:    # O(len(E)) 
        graph1[a].append(b)
        graph2[b].append(a)
    
    for node in range(n):  # O(n)
        if validTree(graph1,n,node):
            return True
    for node in range(n):  # O(n)
        if validTree(graph2,n,node):
            return True
    return False

# Time Complexity = O(n + len(E))
# space complexity = O(n)
n = 5
edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
print(main(n,edges))
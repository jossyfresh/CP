import time
from collections import defaultdict
from collections import deque

def bfs(graph, start):
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
    return main()


def union_find(graph, start):
  parent = {}
  rank = {}
  for node in graph:
    parent[node] = node
    rank[node] = 0

  def find(node):
    if parent[node] != node:
      parent[node] = find(parent[node])
    return parent[node]

  def union(node1, node2):
    parent1 = find(node1)
    parent2 = find(node2)
    if rank[parent1] > rank[parent2]:
      parent[parent2] = parent1
    elif rank[parent1] < rank[parent2]:
      parent[parent1] = parent2
    else:
      parent[parent1] = parent2
      rank[parent1] += 1

  for node in graph:
    for neighbor in graph[node]:
      union(node, neighbor)

  return find(start)

graph = {
  0: [1, 2],
  1: [3, 4],
  2: [5, 6],
  3: [],
  4: [],
  5: [],
  6: []
}

start = 0

bfs_time = time.time()
bfs_visited = bfs(graph, start)
bfs_time = time.time() - bfs_time

union_find_time = time.time()
union_find_visited = union_find(graph, start)
union_find_time = time.time() - union_find_time

print("BFS time:", bfs_time)
print("Union-find time:", union_find_time)
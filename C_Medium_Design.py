import math

class SegmentTree:
  def __init__(self, array):
    self.tree = [math.inf] * (4 * len(array))
    self.build(array)

  def build(self, array):
    for i in range(len(array)):
      self.tree[2 * i + 1] = array[i]

    for i in range(len(array) - 1, -1, -1):
      self.tree[i] = min(self.tree[2 * i + 1], self.tree[2 * i + 2])

  def query_min(self, l, r):
    if l == r:
      return self.tree[l]

    mid = (l + r) // 2
    left_min = self.query_min(l, mid)
    right_min = self.query_min(mid + 1, r)

    return min(left_min, right_min)

def maximum_cost_faster(segments, n, m):
  segments.sort(key=lambda segment: segment[1] - segment[0], reverse=True)
  dp = [[0] * (m + 1) for _ in range(n + 1)]
  for i in range(1, n + 1):
    print(segments[i - 1][0] + 1)
    for j in range(1, segments[i - 1][0] + 1):
      print(i)
      

  return max(dp[n][1:])

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    seg = []
    for _ in range(n):
        l,r = map(int,input().split())
        seg.append((l,r))
    print(maximum_cost_faster(seg,n,m))

#include <ostream>
#include <iostream>
#include <climits>
#include <queue>
#include <set>
#include <unordered_map>

using namespace std;

struct Edge {
  int to, weight;
};

int dijkstra(unordered_map<int, vector<Edge>>& graph, int start) {
  vector<int> distances(graph.size(), INT_MAX);
  distances[start] = 0;
  priority_queue<pair<int, int>> pq;
  pq.push({0, start});

  while (!pq.empty()) {
    int current_distance, current_node;
    tie(current_distance, current_node) = pq.top();
    pq.pop();

    if (distances[current_node] < current_distance) {
      continue;
    }

    for (auto& edge : graph[current_node]) {
      int distance = current_distance + edge.weight;
      if (distance < distances[edge.to]) {
        distances[edge.to] = distance;
        pq.push({distance, edge.to});
      }
    }
  }

  return distances[graph.size() - 1];
}

int main() {
  int n, m, k;
  cin >> n >> m >> k;

  unordered_map<int, vector<Edge>> adjlist;
  for (int i = 0; i < m; i++) {
    int x, y, z;
    cin >> x >> y >> z;
    adjlist[x - 1].push_back({y - 1, z});
    adjlist[y - 1].push_back({x - 1, z});
  }

  int ans = dijkstra(adjlist, 0);

  unordered_map<int, vector<Edge>> adjlist1;
  vector<pair<int, int>> val;
  for (int i = 0; i < k; i++) {
    int x, z;
    cin >> x >> z;
    val.push_back({z, x});
  }

  std::sort(val.begin(), val.end());
  set<int> vi;
  int c = 0;
  for (auto& p : val) {
    if (vi.count(p.second)) {
      c++;
      continue;
    }

    adjlist1[0].push_back({p.second - 1, p.first});
    adjlist1[p.second - 1].push_back({0, p.first});
    vi.insert(p.second);
  }

  int ans1 = dijkstra(adjlist1, 0);

  int count = 0;
  for (int i = 0; i < n; i++) {
    if (ans[i] <= ans1[i] && i != 0 && ans1[i] != INT_MAX) {
      count++;
    }
  }

  cout << count + c << endl;

  return 0;
}

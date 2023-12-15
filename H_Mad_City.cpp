#include <bits/stdc++.h>
using namespace std;
 
// Shorthand notations
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<bool> vb;
typedef vector<vi> vvi;
typedef vector<vl> vvl;
typedef pair<ll, ll> pll;
typedef set<int> si;
typedef set<ll> sl;
typedef priority_queue<int, vector<int>, greater<int>> min_pq;
typedef priority_queue<int> max_pq;
 
// Macros
#define fast_io ios::sync_with_stdio(0); cin.tie(0);
#define FOR(i, n) for (int i = 0; i < n; ++i)
#define FORR(i, n) for (int i = n - 1; i >= 0; --i)
#define forit(it, c) for (__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define forRange(i, a, b) for (int i = (a); i <= (b); ++i)
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define sz(x) (int)x.size()
#define INF 1e9
#define MOD 1000000007
 
/**
 * @author jossy_: YOSEPH-SHEMELES
 * @brief Custom template for CP
 */
template <typename T>
void display(vector<T> &arr) {
    for (auto &i : arr) cout << i << " ";
    cout << endl;
}
 
template <typename T>
void IL(vector<T> &arr, int n) {
    arr.resize(n);
    for (auto &a : arr) cin >> a;
}
// sieve of eratosthenes
void sieve(bool primes[], int x)
{
    primes[1] = false;
 
    // if a number is prime mark all its multiples
    // as non prime
    for (int i=2; i*i <= x; i++)
    {
        if (primes[i] == true)
        {
            for (int j=2; j*j <= x; j++)
                primes[i*j] = false;
        }
    }
}
// gcd
int gcd(int a,int b) {
    if(a == 0)
        return b;
    return gcd(b%a,a);
}



void dfs_cycle(int u, int p, int color[], int par [], int& cyclenumber,unordered_map<int,vector<int>> &adjlist,vector<vector<int>> &cycles)
{
    
    if (color[u] == 2) {
        return;
    }
    if (color[u] == 1) {
        vector<int> v;
        cyclenumber++;
           
        int cur = p;
          v.push_back(cur);
        while (cur != u) {
            cur = par[cur];
              v.push_back(cur);
        }
          cycles.push_back(v);
        return;
    }
    par[u] = p;
 
    color[u] = 1;
 
    for (int v : adjlist[u]) {
        if (v == par[u]) {
            continue;
        }
        dfs_cycle(v, u, color, par, cyclenumber,adjlist,cycles);
    }

    color[u] = 2;
}

void printCycles(int& cyclenumber,vector<vector<int>> &cycles,si &cycle)
{
    for (int i = 0; i < cyclenumber; i++) {
        for (int x : cycles[i])
            cycle.insert(x);
    }
}
vector<int> bfs(int start,unordered_map<int,vector<int>> &adjlist,si &cycle){
    deque<int>dq;
    si vis;
    vector<int>ans(2,-1);
    dq.push_back(start);
    int level = 0;
    while (dq.size() > 0){
        int len = dq.size();
        while (len > 0){
            len -= 1;
            int cur = dq.front();
            if (cycle.find(cur) != cycle.end()){
                ans[0] = cur;
                ans[1] = level;
                return ans;
            }
            dq.pop_front();
            for(auto &node : adjlist[cur]){
                if (vis.find(node) == vis.end()){
                    dq.push_back(node);
                    vis.insert(node);
                }
            }
        }
        level++;
    }
    return ans;
}
int secondbfs(int start,int end,unordered_map<int,vector<int>> &adjlist){
    deque<int>dqi;
    si visits;
    dqi.push_back(start);
    int level = 0;
    while (dqi.size() > 0){
        int len = dqi.size();
        while (len > 0){
            len -= 1;
            int cur = dqi.front();
            if (cur == end){
                return level;
            }
            dqi.pop_front();
            for(auto &node : adjlist[cur]){
                if (visits.find(node) == visits.end()){
                    dqi.push_back(node);
                    visits.insert(node);
                }
            }

        }
        level++;
    }
    return -1;
}
// Main function for solving the problem
void solve() {
    // Start here
    si visited;
    si cycle;
    vector<vector<int>> cycles;
    unordered_map<int,vector<int>>adjlist;
    int n; int a; int b;
    cin >> n >> a >> b;
    int color[n+1];
    int par[n+1];
    int cyclenumber = 0;
    for (int i = 0;i < n;i++){
        int u;int v;
        cin >> u >> v;
        adjlist[u].push_back(v);
        adjlist[v].push_back(u);
    }
    for(int i = 0 ; i < n+1;i++){
        color[i] = 0;
    }
    dfs_cycle(1, 0, color, par, cyclenumber,adjlist,cycles);
    printCycles(cyclenumber,cycles,cycle);
    vector<int>bdist;
    bdist = bfs(b,adjlist,cycle);
    int node = bdist[0];
    int dis = bdist[1];
    int res = secondbfs(a,node,adjlist);
    
    if (res > dis){
        cout << "YES" << endl;
    }
    else{
        cout << "NO" << endl;
    }
}
 
int main() {
    fast_io;
    int t = 1;
    cin >> t;
    while (t--) solve();

    return 0;
}
#include <iostream>
#include <vector>
#include <unordered_map>
#include <climits>

using namespace std;

int n;
vector<pair<int, int>> num;
int total = 0;
unordered_map<string, int> memo;

int dp(int i, int ver, int hor) {
    if (i == n) {
        if (hor >= ver) {
            return hor;
        }
        return INT_MAX;
    }
    string key = to_string(i) + "_" + to_string(ver) + "_" + to_string(hor);
    if (memo.find(key) != memo.end()) {
        return memo[key];
    }
    int a = dp(i+1, ver - num[i].second, hor + num[i].first);
    int b = dp(i+1, ver, hor);
    memo[key] = min(a, b);
    return memo[key];
}

int main() {
    cin >> n;
    num.resize(n);
    for (int i = 0; i < n; i++) {
        cin >> num[i].first >> num[i].second;
        total += num[i].second;
    }
    int ans = dp(0, total, 0);
    cout << ans << endl;
    return 0;
}
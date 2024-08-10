#include <bits/stdc++.h>
// #include <ext/pb_ds/assoc_container.hpp>
// #include <ext/pb_ds/tree_policy.hpp>

using namespace std;
// using namespace __gnu_pbds;

// typedef tree<pair<int, int>, null_type, greater<pair<int, int>>, rb_tree_tag, tree_order_statistics_node_update> ordered_set;
#pragma GCC optimize("O3,Ofast")
#define all(a) (a).begin(), (a).end()
#define ull unsigned long long
#define ll long long

int ceil_div(int a, int b) {
    if (a % b == 0) return a / b;
    else return a / b + 1;
}

struct splitmix_hash {
public:
    size_t operator()(ull x) const {
        static const ull FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
        x += FIXED_RANDOM;
        x += 0x9e3779b97f4a7c15;
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
        x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
        return x ^ (x >> 31);
    }
};

struct pairhash {
public:
    template <typename T, typename U>
    std::size_t operator()(const std::pair<T, U> &x) const {
        int n = std::hash<T>()(x.first) ^ std::hash<U>()(x.second);
        return splitmix_hash()(n);
    }
};

#define MOD 1000000007

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    // insert_numbers(42043ul);
    // int start = 100;
    // for(int i = start; i < start + 20; i++)
    //     insert_numbers(__prime_list[i]);

    const int m = 42043;
    const int mod_rep = 23700;
    const int n = 2e5;
    cout << 1 << '\n';
    cout << n << '\n';
    auto f = [](int i) {
        return (i % mod_rep) * m + (i / mod_rep);
    };
    for (int i = n + 1; i <= n * 2; i++)
        if (i == n * 2) cout << f(i);
        else cout << f(i) << ' ';
    cout << '\n';
    for (int i = 1; i <= n; i++)
        if (i == n) cout << f(i);
        else cout << f(i) << ' ';
    cout << '\n';
    cout << n << '\n';
    for (int i = 1; i < n; i++) 
        cout << f(i) << ' ';
    cout << f(n) << '\n';
}
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
    for (auto &i : arr) cout << i<< " ";
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
// Main function for solving the problem
void solve() {
    // Start here
    map<string,pii>mp;
    double n;
    cin >> n;
    string s;
    cin >> s;
    double left = 0;
    double right = 0;
    vector<pii>ans;
    for (int i = 0; i < n; i++) {
        if (s[i] == '0'){
            left++;
        }
        else{
            right++;
        }
    }
    mp["right"] = {left,right};
    mp["left"] = {0,0};
    double val = mp["left"].first + mp["left"].second;
    double val1 = mp["right"].first + mp["right"].second;
    if ((mp["left"].first >= ceil(val/2)) && (mp["right"].second >= ceil(val1 / 2))){
        double x = n / 2;
        x -= 0;
        ans.push_back({abs(x),0});
    }
    for (int i = 0; i < n; i++) {
        if (s[i] == '0'){
            mp["left"].first++;
            mp["right"].first--;
        }
        else{
            int x = mp["left"].second++;
            int y = mp["right"].second--;
        }
        double val = mp["left"].first + mp["left"].second;
        double val1 = mp["right"].first + mp["right"].second;
        if ((mp["left"].first >= ceil(val/2)) && (mp["right"].second >= ceil(val1 / 2))){
            double y = n / 2;
            y -= (i+1);
            ans.push_back({abs(y),i+1});
        }
   }
   vector<int>res;
   int mins = INF;
   for (int i = 0 ; i < ans.size();i++){
        mins = min(mins,ans[i].first);
   }
   for (int i = 0 ; i < ans.size();i++){
        if (ans[i].first == mins){
            res.push_back(ans[i].second);
        }
   }
   cout << res[0] << endl;
}
 
int main() {
    fast_io;
    int t = 1;
    cin >> t;
    while (t--) solve();

    return 0;
}
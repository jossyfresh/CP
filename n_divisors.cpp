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
#define k 100000
 
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

bool prime[k];
vector<int> primes;
void seive(){
    fill(prime, prime+k, true);
	for(int i = 3; i*i < k; i+=2){
		if(prime[i])
			for(int j = i*i; j < k; j += 2*i)
				prime[j] = false;
	}
	primes.push_back(2);
	for(int i = 3; i < k; i += 2)
		if(prime[i])
			primes.push_back(i);
}
int main(){
    seive();
	int a, b, n; cin >> a >> b >> n;
	long long all_tot = 0;
	for(int i = a; i <= b; i++){
		int res = i;
		long long tot = 1;
		for(int p:primes){
			if(p > res)break;
			int p_tot = 0;
			while(res%p == 0){
				res /= p;
				p_tot += 1;
			}
			tot *= (p_tot + 1);
		}
		if(res > 1)tot *= 2;
		if(tot == n){
			all_tot += 1;
		}
	}
	cout << all_tot;
}
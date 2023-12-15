#include <bits/stdc++.h>
#include <algorithm>
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
void combinationUtil(int arr[], int n, int r, 
                    int index, int data[], int i); 
 

void printCombination(int arr[], int n, int r) 
{ 
    
    int data[r]; 
 
    
    combinationUtil(arr, n, r, 0, data, 0); 
} 
 

void combinationUtil(int arr[], int n, int r, 
                    int index, int data[], int i) 
{ 
 
    if (index == r) 
    { 
        for (int j = 0; j < r; j++) 
            cout << data[j] << " "; 
        cout << endl; 
        return; 
    } 
 
    
    if (i >= n) 
        return; 
 
    data[index] = arr[i]; 
    combinationUtil(arr, n, r, index + 1, data, i + 1); 
    combinationUtil(arr, n, r, index, data, i+1); 
} 
 
// Main function for solving the problem
void solve() {
    // Start here
    int n; int k;
    cin >> n >> k;
    vector<long long> a(n);
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    int evens = 0;
    int five = 5;
    int three = 3;
    int four = 4;
    for (int i = 0; i < n; i++)
    {
        
        if (a[i] % 2 == 0){
            evens ++;
        }
        if (a[i] % 3 == 0){
            three = 0;
        }
        if (a[i] > 3){
            int val = (((a[i]/3)+1)*3)-a[i];
            three = min(val, three);
        }
        if (a[i] <= 3){
            int val = (3) - a[i];
            three = min(val, three);
        }
        if (a[i] % 4 == 0){
            four = 0;
        }
        if (a[i] > 4){
            int val = (((a[i]/4)+1)*4)-a[i];
            four = min(val, four);
        }
        if (a[i] <= 4){
            int val = (4) - a[i];
            four = min(val, four);
        }
        if (a[i] % 5 == 0){
            five = 0;
        }
        if (a[i] > 5){
            int val = (((a[i]/5)+1)*5)-a[i];
            five = min(val, five);
        }
        if (a[i] <= 5){
            int val =  (5) - a[i];
            five = min(val, five);
        }
    }
    if (k==2){
        if (evens > 0){
            cout << 0 <<endl;
        }
        else{
            cout << 1 <<endl;
        }
    }
    else if (k==3){
        cout << three << endl;
    }
    else if (k==4){
        int val = four;
        if (evens > 1){
            val = min(val,0);     
        }
        else if (evens > 0 && n > 1){
            val = min(val,1);    
        }
        cout << min(val,2) << endl;
        
    }
    else{

        cout << five << endl;
    }
}
 
int main() {
    fast_io;
    int t = 1;
    
    while (t--){
        int arr[] = {1, 2, 4, 4, 5}; 
    int r = 3; 
    int n = sizeof(arr)/sizeof(arr[0]); 
    cout<<n<<endl;
    printCombination(arr, n, r); 
    }

    return 0;
}
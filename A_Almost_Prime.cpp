#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
const int N = 2e5 + 5;
 
int n, q;
char a[N], b[N];
int cntA[26][N], cntB[26][N];
 
void solve() {
    cin >> n >> q;
    cin >> a >> b;
 
    for (int i = 0; i < 26; i++) {
        for (int j = 0; j <= n; j++) {
            cntA[i][j] = cntB[i][j] = 0;
        }
    }
 
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 26; j++) {
            cntA[j][i + 1] = cntA[j][i];
            cntB[j][i + 1] = cntB[j][i];
        }
        cntA[a[i] - 'a'][i + 1]++;
        cntB[b[i] - 'a'][i + 1]++;
    }
 
    while (q--) {
        int l, r;
        cin >> l >> r;
        l--;
        int ans = 0;
 
        for (int i = 0; i < 26; i++) {
            int countA = cntA[i][r] - cntA[i][l];
            int countB = cntB[i][r] - cntB[i][l];
            if (countB > countA) {
                ans += countB - countA;
            }
        }
 
        cout << ans << "\n";
    }
}